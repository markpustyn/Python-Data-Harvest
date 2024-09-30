#!/usr/bin/perl

use strict;
use warnings;

sub userInput {
    my @a = ("Print: Raw HTML data from given URL", "Images: Download to system or extract images Url to Database",
                "MetaData: Get url metadata stored to database", "Links: Get all links given url store to Database", "All: Perform all tasks above");
    print "Enter the URL of the website: ";
    my $url = <STDIN>;
    chomp $url;
    print "Options:\n";
    for (my $i = 1; $i <= scalar @a; $i++) {
        print "$i. $a[$i-1]\n";
    }
    print "Enter the desired format (1-5): ";
    my $format_choice = <STDIN>;
    chomp $format_choice;
    return ($url, $format_choice);
}

my ($url, $format_choice) = userInput();
open(my $fh, ">", "input.txt") or die "Could not open file 'input.txt' $!";

print $fh "$url\n$format_choice\n";

close $fh;

print "URL and format choice was succesfully written\n";

