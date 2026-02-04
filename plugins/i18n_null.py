"""
Minimal plugin to install null (pass-through) translations for Jinja2 i18n
extension. Replaces i18n_subsites for single-language English sites.

The pelican-bootstrap3 theme uses {% trans %} tags in its templates,
which require the Jinja2 i18n extension and gettext translations to be
installed. This plugin provides identity translations so that all strings
pass through unchanged.

TODO: Remove when theme is migrated (feature 002/003).
"""

from pelican import signals


def install_null_translations(generator):
    generator.env.install_null_translations()


def register():
    signals.generator_init.connect(install_null_translations)
