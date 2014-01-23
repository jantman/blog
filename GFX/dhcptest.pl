#!/usr/bin/perl

use IO::Socket::INET;
use Net::DHCP::Packet;
use Net::DHCP::Options;
use Net::DHCP::Constants;

my $socket = IO::Socket::INET->new(Proto     => 'udp',
                                   Broadcast => 1,
                                   PeerPort  => '67',
                                   LocalPort => '68',
                                   PeerAddr  => '255.255.255.255')
    or die ($@);

# create and send DHCP Packet
$disc = Net::DHCP::Packet->new(xid => int(rand(0xFFFFFFFF)),
				  op => BOOTREQUEST(),
				  Htype => 0x01,
				  Hlen => 0x06,
				  Hops => 0x01,
				  Flags => 0x0,
				  Ciaddr => '0.0.0.0',
				  Yiaddr => '0.0.0.0',
				  Siaddr => '0.0.0.0',
				  Giaddr => '172.16.58.65',
				  DHO_DHCP_MESSAGE_TYPE() => DHCPDISCOVER())
    or die "Can't create DHCP discover packet: $!";

if(@ARGV > 0)
{
    if ($ARGV[0] eq "new") {
	print "NEW packet\n";
	new();
    } elsif ($ARGV[0] eq "original") {
	print "ORIGINAL packet\n";
	original();
    } elsif($ARGV[0] eq "laptop") {
	print "LAPTOP packet\n";
	laptop();
    } else {
	exit;
    }
}
else
{
    print "USAGE: dhcptest.pl (laptop|new|original)\n";
    exit;
}

print $disc->toString();
print "\n\n";

$socket->send($disc->serialize())
    or die "Can't send DHCP discover packet: $!";

print "Sent packet.\n";
exit;

sub original
{
    $disc->chaddr('00163E0CCF08');
    $disc->secs(0);

    $disc->addOptionRaw(0x39, chr(0x05).chr(0xDC)); # option 57 - Maximum DHCP message size
    $disc->addOptionValue(0x3c, "Etherboot-5.4");  # option 60 - Vendor Class Identifier
    $disc->addOptionRaw(0x37, chr(0x01).chr(0x03).chr(0x0c).chr(0x2b)); # option 55 - Parameter Request List
    $disc->addOptionValue(0x96, chr(0xaf).chr(0x05).chr(0x01).chr(0x10).chr(0xec).chr(0x81).chr(0x39).chr(0xb1).chr(0x02).chr(0x03).chr(0x00)); # option 150 - TFTP Server Address (Etherboot)
}

sub new
{
    $disc->chaddr('00163E0CCF08');
    $disc->secs(2);

    $disc->addOptionRaw(0x39, chr(0x05).chr(0xDC)); # option 57 - Maximum DHCP message size
    $disc->addOptionValue(0x3c, "Etherboot-5.4");  # option 60 - Vendor Class Identifier
    $disc->addOptionRaw(0x37, chr(0x01).chr(0x03).chr(0x0c).chr(0x2b)); # option 55 - Parameter Request List
    $disc->addOptionValue(0x96, chr(0xaf).chr(0x05).chr(0x01).chr(0x10).chr(0xec).chr(0x81).chr(0x39).chr(0xb1).chr(0x02).chr(0x03).chr(0x00)); # option 150 - TFTP Server Address (Etherboot)
}

sub laptop
{
    $disc->chaddr('000D60B0769B');
    $disc->secs(21);

    # option 55 - Parameter Request List
    my $paramList = chr(0x01).chr(0x1c).chr(0x03).chr(0x1a).chr(0x0c).chr(0x0f).chr(0x06).chr(0x28).chr(0x29).chr(0x57).chr(0x55).chr(0x56).chr(0x2c).chr(0x2d).chr(0x2e).chr(0x2f).chr(0x2a);
    $disc->addOptionRaw(0x37, $paramList);
}
