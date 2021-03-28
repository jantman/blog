Title: Migrating Kodi to MariaDB, with locked-down permissions and no import/export
Date: 2021-03-28 10:55
Modified: 2021-03-28 10:55
Author: Jason Antman
Category: Software
Tags: kodi, osmc, database, mysql, mariadb
Slug: migrating-kodi-to-mariadb-with-locked-down-permissions-and-no-importexport
Summary: Instructions for migrating Kodi from SQLite to MySQL/MariaDB, without giving root database permissions or needing import/export of media.

For the past two years or so, I've been using [Kodi](https://kodi.tv/) to power my television. It works great, as I don't have cable and all of my DVDs have been ripped to a hard drive. It lets me watch any of my digital movies/TV shows, as well as Netflix and Amazon Prime Video - which is all that I need. Kodi itself is running on a Raspberry Pi 4 in a tiny little case, so it works great for a media center / HTPC. I recently wanted to add another Kodi device for my bedroom TV, but unfortunately (unlike the older [MythTV](https://www.mythtv.org/), that I used years ago) Kodi isn't a client/server app, it's just a single local program.

Using multiple front-ends is sort of supported by [switching from the built-in SQLite database to MySQL](https://kodi.wiki/view/MySQL), but there's a fair amount left out (such as addons). The process for switching to a MySQL-compatible database server also had some pain points for me, namely that it requires complete root permissions on the database and it relies on exporting and then re-importing all of your media. The first point (database permissions) is untenable, since my MariaDB server contains a number of other databases, some of which have private information in them. The second point - exporting information on all of the media, then switching from SQLite to MariaDB, then re-importing everything - just seemed horribly inefficient.

So, here's the process I used for switching Kodi from SQLite to MariaDB and adding a second frontend. This assumes that you already have your media/library stored remotely and mounted via NFS, and that your two frontend devices (Raspberry Pi 4's for me) are running the exact same OS, Kodi version, and versions of everything else (for me, it's Raspberry Pi OS, everything updated to latest).

**tl;dr:** Point Kodi to a temporary MySQL server to create the schema. Use a Python script to SELECT every row from the SQLite DBs and INSERT them into MySQL. ``mysqldump`` the result and import it into your production DB server. Done.

1. Identify the exact database server version you're going to be using. For me, this is MariaDB 10.5.9.
2. Stand up another, brand new and empty, server running that version. For ease, I'm using the Docker container for ``mariadb:10.5.9`` running on my laptop. Expose the port (3306) to your network. If running in Docker, make sure you mount a directory into the container. For me, this was ``docker run -it --rm --name db -v /tmp:/host-tmp -p 3306:3306 -e MYSQL_ROOT_PASSWORD=foobar mariadb:10.5.9``
3. Do whatever you need to, to get port 3306 passed through your firewall and available to the Kodi hosts.
4. Stop/exit Kodi on the existing host.
5. Back up your entire Kodi directory (``~/.kodi``) somewhere. Copy the SQLite database files (``.kodi/userdata/Database``) to the computer you're working on. Also rename or move the ``MyMusic72.db`` and ``MyVideos116.db`` files from the ``Database`` directory, so we can be sure that we're using MySQL later on.
6. Get a root session on your temporary database; for me, this is ``docker exec -it db mysql -uroot -p``
7. Set up permissions for kodi as described in [the documentation](https://kodi.wiki/view/MySQL/Setting_up_MySQL): ``CREATE USER 'kodi' IDENTIFIED BY 'kodi'; GRANT ALL ON *.* TO 'kodi'; flush privileges;``
8. Run ``SHOW DATABASES;`` - this should list 3 default databases: information_schema, mysql, and performance_schema
9. On the Kodi host, create ``~/.kodi/userdata/advancedsettings.xml`` with the [appropriate content for MySQL](https://kodi.wiki/view/MySQL/Setting_up_Kodi) pointing to your test/temporary DB. Start Kodi back up.
10. You should get a blank, empty Kodi main screen, but on your temporary DB server you should see two new databases. For Kodi 18 (Leia) they will be called ``MyMusic72`` and ``MyVideos116``. Once this is done, stop Kodi again.
11. Save the ``sqlite-to-mysql.py`` script, below, to the same directory as your database backups. This script is written for Python 3.7 or later, and needs the [PyMySQL](https://pymysql.readthedocs.io/en/latest/) (``pip install PyMySQL``) package.
12. Run ``python3 sqlite-to-mysql.py`` to copy all data from the SQLite databases to MySQL/MariaDB on the **temporary** database server. Run first with ``-h`` to see the available options and their default values.
13. Start Kodi back up. You should see all of your library, your watched history and current positions, etc. That means... it worked! Stop kodi on all frontends.
14. On the temporary database server, dump both databases. For me, this was ``docker exec -it db /bin/bash`` then ``cd /host-tmp`` then ``mysqldump --insert-ignore --routines --triggers --databases MyMusic72 MyVideos116 -uroot -p > kodi-data.sql``
15. Copy the resulting SQL dump file (``kodi-data.sql``) to your actual database server and restore it.
16. Update ``~/.kodi/userdata/advancedsettings.xml`` to point to your production database server.
17. Now, copy all of ``~/.kodi`` from the primary frontend that you've been working on to all others. This will update them with not only your database configuration but also your addons, settings, etc.
18. Start up all Kodi frontends; they should now be functional and synchronized.

## Upgrading

Upgrading will be a bit less of a pain, but still not fun:

1. Dump your databases from MySQL/MariaDB, stand up another temporary DB server, restore the dump. Give Kodi full privileges.
2. Stop all of your Kodi frontends.
3. Switch one of your Kodi frontends to the temporary server, upgrade Kodi, start it up, let it upgrade the database.
4. Dump the database, restore it on your production server. Adjust permissions for new database names as needed.
5. Point your running Kodi instance back to the production server.
6. Upgrade all remaining frontends and start them up.

## sqlite-to-mysql.py

```python
#!/usr/bin/env python
"""
Script for migrating Kodi SQLite databases to MySQL / MariaDB.

Requires Python >= 3.7 and PyMySQL.

For usage, see:
https://blog.jasonantman.com/2021/03/migrating-kodi-to-mariadb-with-locked-down-permissions-and-no-importexport/

NOTE: This currently ignores triggers, as all triggers that Kodi currently uses
in these DBs are AFTER delete.
"""

import sys
import argparse
import logging
from typing import Any, List, Tuple

import pymysql
import pymysql.cursors
import sqlite3

FORMAT: str = "[%(asctime)s %(levelname)s] %(message)s"
logging.basicConfig(level=logging.WARNING, format=FORMAT)
logger: logging.Logger = logging.getLogger()


class KodiMigrator:

    def __init__(
        self, host: str, port: int, user: str, passwd: str,
        dry_run: bool = False
    ):
        self.dry_run: bool = dry_run
        logger.debug(
            'Connecting to MySQL at %s:%s as %s', host, port, user
        )
        self.mysql: pymysql.connections.Connection = pymysql.connect(
            host=host,
            user=user,
            port=port,
            password=passwd,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        logger.info('Connected to MySQL')

    def run(self):
        for dbname in ['MyMusic72', 'MyVideos116']:
            self.handle_db(dbname)

    def handle_db(self, dbname: str):
        logger.info('Handling database: %s', dbname)
        logger.debug('MySQL select DB %s', dbname)
        self.mysql.select_db(dbname)
        mysql_tables = self._mysql_table_names()
        logger.debug('SQLite3 open %s.db', dbname)
        local: sqlite3.Connection = sqlite3.connect(f'{dbname}.db')
        sqlite_tables = self._sqlite_table_names(local)
        local.row_factory = sqlite3.Row
        if mysql_tables != sqlite_tables:
            raise RuntimeError(
                f'ERROR: MySQL table names in {dbname} ({mysql_tables}) do '
                f'not match SQLite table names ({sqlite_tables})!'
            )
        with self.mysql.cursor() as cursor:
            cursor.execute('set FOREIGN_KEY_CHECKS = 0;')
            self._fix_db(dbname, cursor)
            for tname in mysql_tables:
                self._handle_table(local, cursor, tname)
            cursor.execute('set FOREIGN_KEY_CHECKS = 1;')
            self.mysql.commit()

    def _fix_db(self, dbname: str, cur: pymysql.cursors.DictCursor):
        if dbname != 'MyVideos116':
            return
        # for data conversion, change tvshow.c06 from TEXT to MEDIUMTEXT
        self._mysql_execute(
            cur, 'ALTER TABLE tvshow MODIFY COLUMN c06 MEDIUMTEXT;'
        )

    def _handle_table(
        self, local: sqlite3.Connection, cur: pymysql.cursors.DictCursor,
        table_name: str
    ):
        # first empty the MySQL table
        self._mysql_execute(cur, f'DELETE FROM {table_name};')
        # now get the data from SQLite and copy it over
        sql = f'SELECT * FROM {table_name};'
        logger.debug('SQLite execute: %s', sql)
        local_cur: sqlite3.Cursor = local.cursor()
        local_cur.execute(sql)
        count: int = 0
        for row in local_cur:
            if table_name == 'tvshow' and row['idShow'] == 3:  # Doctor Who - c06 too long
                continue
            tmp = self._mysql_insert_for_row(table_name, row)
            self._mysql_execute(cur, *tmp)
            count += 1
        logger.info('Copied %d rows for table %s', count, table_name)

    def _mysql_insert_for_row(
        self, tname: str, row: sqlite3.Row
    ) -> Tuple[str, Tuple]:
        keys: List[str] = []
        values: List[str] = []
        for k, v in dict(row).items():
            keys.append(k)
            values.append(v)
        sql = f'INSERT INTO {tname} ({", ".join(keys)}) VALUES (' \
              f'{", ".join(["%s" for x in values])});'
        return sql, tuple(values)

    def _mysql_execute(
        self, cur: pymysql.cursors.Cursor, sql: str, data: tuple = ()
    ):
        if self.dry_run:
            logger.warning('DRY RUN: MySQL Execute: %s %s', sql, data)
        else:
            logger.debug('MySQL Execute: %s %s', sql, data)
            try:
                cur.execute(sql, data)
            except pymysql.err.MySQLError:
                logger.error('Error in query: %s %s', sql, data)
                raise

    def _sqlite_table_names(self, db: sqlite3.Connection) -> List[str]:
        cursor: sqlite3.Cursor = db.cursor()
        sql: str = "SELECT name FROM sqlite_master WHERE type='table';"
        logger.debug('SQLite execute: %s', sql)
        cursor.execute(sql)
        res: List[str] = sorted([x[0] for x in cursor.fetchall()])
        logger.debug('SQLite tables: %s', res)
        return res

    def _mysql_table_names(self) -> List[str]:
        sql: str = "show full tables where Table_Type != 'VIEW'"
        logger.debug('MySQL execute: %s', sql)
        with self.mysql.cursor(cursor=pymysql.cursors.Cursor) as cursor:
            cursor.execute(sql)
            res: List[str] = sorted([x[0] for x in cursor.fetchall()])
        logger.debug('MySQL tables: %s', res)
        return res


def parse_args(argv):
    """
    parse arguments/options

    this uses the new argparse module instead of optparse
    see: <https://docs.python.org/2/library/argparse.html>
    """
    p = argparse.ArgumentParser(description='Migrate Kodi SQLite to MySQL')
    p.add_argument('-d', '--dry-run', dest='dry_run', action='store_true',
                   default=False,
                   help="dry-run - print SQL that would be sent to MySQL but "
                        "don't actually run it")
    p.add_argument('-v', '--verbose', dest='verbose', action='store_true',
                   help='debug-level output.', default=False)
    p.add_argument('-H', '--host', type=str, dest='host',
                   help='MySQL host (default: 127.0.0.1)', default='127.0.0.1')
    p.add_argument('-P', '--port', type=int, dest='port', default=3306,
                   help='MySQL port (default: 3306)')
    p.add_argument('-u', '--user', type=str, dest='user', default='kodi',
                   help='MySQL user (default: kodi)')
    p.add_argument('-p', '--passwd', type=str, dest='passwd', default='kodi',
                   help='MySQL password (default: kodi)')
    args = p.parse_args(argv)
    return args


def set_log_info():
    """set logger level to INFO"""
    set_log_level_format(logging.INFO,
                         '%(asctime)s %(levelname)s:%(name)s:%(message)s')


def set_log_debug():
    """set logger level to DEBUG, and debug-level output format"""
    set_log_level_format(
        logging.DEBUG,
        "%(asctime)s [%(levelname)s %(filename)s:%(lineno)s - "
        "%(name)s.%(funcName)s() ] %(message)s"
    )


def set_log_level_format(level, format):
    """
    Set logger level and format.

    :param level: logging level; see the :py:mod:`logging` constants.
    :type level: int
    :param format: logging formatter format string
    :type format: str
    """
    formatter = logging.Formatter(fmt=format)
    logger.handlers[0].setFormatter(formatter)
    logger.setLevel(level)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])

    # set logging level
    if args.verbose:
        set_log_debug()
    else:
        set_log_info()
    KodiMigrator(
        args.host, args.port, args.user, args.passwd, dry_run=args.dry_run
    ).run()

```
