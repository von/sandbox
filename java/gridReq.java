
// ----------------------------------------------------------------------
// This code is developed as part of the Java CoG Kit project
// The terms of the license can be found at http://www.cogkit.org/license
// This message may not be removed or altered.
// ----------------------------------------------------------------------

/**
 * Copyright (c) 2003, National Research Council of Canada
 * All rights reserved.
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy of this 
 * software and associated documentation files (the "Software"), to deal in the Software 
 * without restriction, including without limitation the rights to use, copy, modify, merge, 
 * publish, distribute, and/or sell copies of the Software, and to permit persons to whom the 
 * Software is furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice(s) and this licence appear in all copies of the Software or 
 * substantial portions of the Software, and that both the above copyright notice(s) and this 
 * license appear in supporting documentation.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
 * OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
 * NONINFRINGEMENT OF THIRD PARTY RIGHTS. IN NO EVENT SHALL THE 
 * COPYRIGHT HOLDER OR HOLDERS INCLUDED IN THIS NOTICE BE LIABLE 
 * FOR ANY CLAIM, OR ANY DIRECT, INDIRECT, SPECIAL OR CONSEQUENTIAL 
 * DAMAGES, OR ANY DAMAGES WHATSOEVER (INCLUDING, BUT NOT 
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS 
 * OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWSOEVER 
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN AN ACTION OF 
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
 * OTHERWISE) ARISING IN ANY WAY OUT OF OR IN CONNECTION WITH THE 
 * SOFTWARE OR THE USE OF THE SOFTWARE, EVEN IF ADVISED OF THE 
 * POSSIBILITY OF SUCH DAMAGE.
 * 
 * Except as contained in this notice, the name of a copyright holder shall NOT be used in 
 * advertising or otherwise to promote the sale, use or other dealings in this Software 
 * without specific prior written authorization.  Title to copyright in this software and any 
 * associated documentation will at all times remain with copyright holders.
 */


//package org.globus.cog.security.cert.request;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.PrivateKey;
import java.security.PublicKey;
import org.bouncycastle.asn1.DERConstructedSet;
import org.bouncycastle.asn1.x509.X509Name;
import org.bouncycastle.jce.PKCS10CertificationRequest;
//import org.bouncycastle.util.encoders.Base64;
//import org.globus.common.CoGProperties;
//import org.globus.gsi.CertUtil;
//import org.globus.cog.security.cert.request.OpenSSLKey;
import org.globus.gsi.OpenSSLKey;
import org.globus.gsi.bc.BouncyCastleOpenSSLKey;
//import org.globus.util.PEMUtils;
//import org.globus.util.Util;

import java.util.StringTokenizer;

/**
 * GridCertRequest Command Line Client
 * 
 * Things remaining to be done:
 * Support for host or service certificate request. Perhaps this should not be
 * part of this tool since the COG kit is mostly a client library.
 * Prompt user for each component of the DN. (Interactive mode)
 * @author Jean-Claude Cote
 */
public final class gridReq {

    public static void main(String[] args) {
        String cn = "Von Welch";
        String password = "null";
        String userKeyFile = "/tmp/key";
        String userCertFile = "/tmp/cert";
        String userCertReqFile = "/tmp/req";

        try {
            System.out.println("writing new private key to " + userKeyFile);
            genCertificateRequest(
                cn,
                "ca@gridcanada.ca",
                password,
                userKeyFile,
                userCertFile,
                userCertReqFile);
        } catch (Exception e) {
            System.out.println("error: " + e);
            e.printStackTrace();
        }
    }

    /**
     * Generates a encrypted private key and certificate request.
     */
    static public void genCertificateRequest(
        String dname,
        String emailAddressOfCA,
        String password,
        String privKeyLoc,
        String certLoc,
        String certReqLoc)
        throws Exception {

        String sigAlgName = "MD5WithRSA";
        String keyAlgName = "RSA";

        //CertUtil.init();

        // Generate a new key pair.
        KeyPairGenerator keygen = KeyPairGenerator.getInstance(keyAlgName);
        KeyPair keyPair = keygen.genKeyPair();
        PrivateKey privKey = keyPair.getPrivate();
        PublicKey pubKey = keyPair.getPublic();

        // Generate the certificate request.        
        X509Name name = new X509Name(dname);
        DERConstructedSet derSet = new DERConstructedSet();
        PKCS10CertificationRequest request =
            new PKCS10CertificationRequest(
                sigAlgName,
                name,
                pubKey,
                derSet,
                privKey);

        // Save the certificate request to a .pem file.
        byte[] data = request.getEncoded();
        PrintStream ps = new PrintStream(new FileOutputStream(certReqLoc));

        // build / delimited name.        
        String certSubject = "";
        StringTokenizer tokens = new StringTokenizer(dname, ",");
        while(tokens.hasMoreTokens()){
            certSubject = certSubject + "/" + tokens.nextToken();
        }

        ps.print( "\n\n"
            + "Please mail the following certificate request to " + emailAddressOfCA + "\n"
            + "\n"
            + "==================================================================\n"
            + "\n"
            + "Certificate Subject:\n"
            + "\n"
            + certSubject
            + "\n"
            + "\n"
            + "The above string is known as your user certificate subject, and it \n"
            + "uniquely identifies this user.\n"
            + "\n"
            + "To install this user certificate, please save this e-mail message\n"
            + "into the following file.\n"
            + "\n"
            + "\n"
            + certLoc
            + "\n"
            + "\n"
            + "\n"
            + "      You need not edit this message in any way. Simply \n"
            + "      save this e-mail message to the file.\n"
            + "\n"
            + "\n"
            + "If you have any questions about the certificate contact\n"
            + "the Certificate Authority at " + emailAddressOfCA + "\n"
            + "\n");
        ps.print(toPEM(data));
        ps.close();

        // Save private key to a .pem file.
        OpenSSLKey key = new BouncyCastleOpenSSLKey(privKey);
        if (password.length() != 0) {
            key.encrypt(password);
        }
        key.writeTo(new File(privKeyLoc).getAbsolutePath());
        // set read only permissions
        //Util.setFilePermissions(privKeyLoc, 600);

        // Create an empty cert file.
        File f = new File(certLoc);
        f.createNewFile();
    }

    /**
     * Converts to PEM encoding.
     */
    static public String toPEM(byte[] data) {
        byte[] enc_data = Base64.encode(data);
        String header = "-----BEGIN CERTIFICATE REQUEST-----";
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        try {
            PEMUtils.writeBase64(
                out,
                header,
                enc_data,
                "-----END CERTIFICATE REQUEST-----");
        } catch (IOException e) {
            throw new RuntimeException("Unexpected error: " + e.getMessage());
        }
        return new String(out.toByteArray());
    }

}
