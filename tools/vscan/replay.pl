#!/usr/bin/perl
use Getopt::Long;
use JSON::PP;
require 'plugins/LW2.pm';
my ($infile, $proxy, %request, $header, %result, $s_request);
LW2::http_init_request(\%request);

# options
GetOptions("help"    => \&usage,
           "file=s"  => \$infile,
           "proxy=s" => \$proxy
           );

if (($infile eq '') && (-r $ARGV[0])) {
    $infile = $ARGV[0];
}

if ($infile eq '') { usage(); }

# load save file
if (!-r $infile) {
    print "ERROR: Argument 1 should be '-help' or a Nikto save file\n\n";
    exit;
}

open(INFILE, "<$infile") || die print "Unable to open file: $!\n\n";
while (<INFILE>) {
    if ($_ =~ /^(((Test|OSVDB) ID)|Message):/) { $header .= $_; next; }
    next unless $_ =~ /^REQUEST:/;
    chomp;
    $_ =~ s/^REQUEST://;
    $s_request = JSON::PP->new->utf8(1)->allow_nonref(1)->decode($_);
    if (ref($s_request) ne 'HASH') {
        print "ERROR: Unable to read JSON into request structure\n";
        exit;
    }
}
close(INFILE);

# set into request hash
foreach my $key (keys %{$s_request}) {
    $request{$key} = $s_request->{$key};
}

# proxy
if ($proxy ne '') {
    my @p = split(/:/, $proxy);
    if (($p[0] eq '') || ($p[1] eq '') || ($p[1] =~ /[^\d]/)) {
        print "ERROR: Invalid proxy designation\n";
        exit;
    }
    $request{'whisker'}->{'proxy_host'} = $p[0];
    $request{'whisker'}->{'proxy_port'} = $p[1];
}

# output for the user
print "-" x 44, "  Info\n";
print "Request to:     http";
print "s" if $request->{'whisker'}->{'ssl'};
print "://"
  . $request{'whisker'}->{'host'} . ":"
  . $request{'whisker'}->{'port'}
  . $request{'whisker'}->{'uri'} . "\n";
print $header;

# make request
LW2::http_fixup_request(\%request);
LW2::http_do_request_timeout(\%request, \%result);

# output for the user
print "-" x 44, "  Response\n";

foreach my $k (@{ $result{'whisker'}->{'header_order'} }) {
    print "$k: " . $result{$k} . "\n";
}

print "\n$result{'whisker'}->{'data'}\n\n";

###############################################################################
sub usage {
    print "replay.pl -- Replay a saved scan result\n";
    print "     -file 		Parse request from this file\n";
    print "     -proxy		Send request through this proxy (format: host:port)\n";
    print "     -help		Help output\n";
    exit;
}
