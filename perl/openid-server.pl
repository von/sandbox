#!/usr/bin/perl
######################################################################
#
# A basic OpenId consumer based on Net::OpenID::Consumer.
#
# Kudos:
# http://www.lemoda.net/perl/openid/net-openid.html
#
######################################################################

use warnings;
use strict;
use Net::OpenID::Consumer;
use LWP::UserAgent;
use CGI;
use CGI::Carp 'fatalsToBrowser';

my $cgi = CGI::new();

my $mode = $cgi->param("mode");
my $url = $cgi->url();
my $baseURL = $cgi->url(-base => 1);

if ($mode eq "init")
{
    my $openid = $cgi->param("openid");

    # Do a quickie check of the input
    fail ('No OpenID')  if ! $openid;
    # I'm not sure this regex is a perfect solution.
    fail ('Bad OpenID') if $openid =~ /[^a-z0-9\._:\/-]/i;

    my $consumer = newConsumer();
    my $claimed_id = $consumer->claimed_identity($openid);
    if (!$claimed_id)
    {
	fail("Cannot parse claimed identity", $consumer->errocode());
    }
    my $check_url = $claimed_id->check_url (
	# The place we go back to.
	return_to  => $url,
	# Having this simplifies the login process.
	trust_root => $baseURL,
    );
    # Automatically redirect the user to the endpoint.
    print $cgi->redirect ($check_url);
}
else
{
    my $consumer = newConsumer();
    
    $consumer->handle_server_response(
	not_openid => sub {
	    print $cgi->header();
	    print $cgi->start_html();
	    print <<EOS;
<form action="$url" method="GET" target="_blank">
<input type="text" name="openid">
<input type="hidden" name="mode" value="init">
<input type="submit" value="Run send.cgi">
</form>
<p>BaseURL: $baseURL</p>
<p>URL: $url</p>
EOS
;
	    print $cgi->end_html();
	},
	setup_required => sub {
	    my $setup_url = shift;
	    print $cgi->header(), $cgi->start_html();
	    print "You need to do something <a href='$setup_url'>here</a>.";
	    print $cgi->end_html();
	},
	cancelled => sub {
	    print $cgi->header(), $cgi->start_html();
	    print 'You cancelled your login.\n';
	    print $cgi->end_html();
	},
	verified => sub {
	    my $vident = shift;
	    my $url = $vident->url;
	    print $cgi->header(), $cgi->start_html();
	    print "You are verified as '$url'.";
	    print $cgi->end_html();
	},
	error => sub {
	    my $err = shift;
	    print $cgi->header(), $cgi->start_html();
	    print "Error: $err";
	    print $cgi->end_html();

	}
	);
}
exit 0;

sub newConsumer
{
    my $csr = Net::OpenID::Consumer->new(
	# The user agent which sends the openid off to the server.
	ua    => LWP::UserAgent->new,
	# Who we are.
	required_root => $baseURL,
	# Our password.
	consumer_secret => 'xYZabC0123',
	args => $cgi,
	);
    return $csr;
}

sub fail
{
    my ($message, $errcode) = @_;
    print $cgi->header, $cgi->start_html();
    print "<h1>There was a problem</h1>\n";
    print "<p><b>$message</b></p>\n";
    if ($errcode) {
        print "<p>The error code was <code>$errcode</code></p>\n";
    }
    print $cgi->end_html;
    exit 0;
}


