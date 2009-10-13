#!/usr/bin/perl -w

# Requires IO::Socket::SSL
# http://search.cpan.org/~sullr/IO-Socket-SSL-1.01/SSL.pm
# Net::SSLeay

use Globus::MyProxyClient;
use Globus::GSISocket;
use Globus::GSICredential;

# being called by user, generated certificate request
use Crypt::OpenSSL::PKCS10;

my $req = Crypt::OpenSSL::PKCS10->new();
# Use dummy DN, GridShib-CA will override with correct value
$req->set_subject("/C=US/O=Dummy/CN=Dummy");
$req->sign();
my $reqPem = $req->get_pem_req();;

$Globus::GSISocket::DEBUG = 1;
$Globus::MyProxyClient::DEBUG = 1;

my $client = Globus::MyProxyClient->new(ServerHost =>"computer.ncsa.uiuc.edu");

if (!$client) {
  die "I encountered a problem: ",
    Globus::MyProxyClient::errstr();
}

my $cred = $client->getCred(
    Username => "vwelch",
    Passphrase => "test",
    Lifetime => 3600,
    CertReq => _convertReqToDER($reqPem),
    CertReqFormat => "DER");

if (!defined($cred))
{
    die "Error getting credential: " . $client->errstr();
}

my @certs = $cred->getDERCerts();
foreach $cert (@certs)
  {
    print _convertCertToPEM($cert);
  }



######################################################################
#
# Conversion routines to convert from DER to/from PEM
# These call out to openssl, which is a pain, but there doesn't seem
# to be a native way to accomplish this.

sub _convertReqToDER {
    my $reqPEM = shift;
    use IPC::Open3;

    local(*cmdIn, *cmdOut, *cmdErr);

    my $pid = IPC::Open3::open3(\*cmdIn, \*cmdOut, \*cmdErr,
				"openssl", "req",
				"-inform", "PEM",
				"-outform", "DER");

    print cmdIn $reqPEM;
    close(cmdIn);

    my $data = "";
    my $offset = 0;
    my $read;
    while(($read = read(cmdOut, $data, 512, $offset)) > 0)
    {
	$offset += $read;
    }
    close(cmdOut);
    while(<cmdErr>)
    {
	print;
    }
    return $data;
}


sub _convertCertToPEM {
    my $der = shift;
    use IPC::Open3;

    local(*cmdIn, *cmdOut, *cmdErr);

    my $pid = IPC::Open3::open3(\*cmdIn, \*cmdOut, \*cmdErr,
			    "openssl", "x509",
			    "-inform", "DER",
			    "-outform", "PEM");

    print cmdIn $der;
    close(cmdIn);
    
    my $data = "";
    my $offset = 0;
    my $read;
    while(($read = read(cmdOut, $data, 512, $offset)) > 0)
    {
	$offset += $read;
    }
    close(cmdOut);
    
    while(<cmdErr>)
    {
	print;
    }
    return $data;
}

