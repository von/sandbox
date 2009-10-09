import java.security.KeyPairGenerator;
import java.security.KeyPair;
import java.security.PublicKey;
import java.security.PrivateKey;
import sun.security.pkcs.PKCS10;
import java.lang.reflect.Method;
import java.security.Security;
import java.security.Provider;
import java.security.Signature;
import java.io.ByteArrayOutputStream;
import java.io.ByteArrayInputStream;
import java.io.PrintStream;

import org.bouncycastle.asn1.x509.X509Name;
import org.bouncycastle.asn1.ASN1Sequence;
import org.bouncycastle.asn1.DERSet;
import org.bouncycastle.asn1.DERObject;
import org.bouncycastle.asn1.pkcs.PrivateKeyInfo;
import org.bouncycastle.asn1.DERInputStream;
import org.bouncycastle.asn1.DEROutputStream;
import org.bouncycastle.util.encoders.Base64;
import org.bouncycastle.jce.PKCS10CertificationRequest;
import org.bouncycastle.jce.provider.BouncyCastleProvider;

public class test {
    // Size of private key to generate
    static int keySize = 1024;

    // Key algorithm to use
    static String keyAlg = "RSA";
    static String sigAlgName = "MD5withRSA";

    static String dname = "CN=Von Welch";
    static String provider = "SunRsaSign";

    public static void main(String[] args)
    {
        try
        {
            KeyPairGenerator keyGenerator = KeyPairGenerator.getInstance(keyAlg);
            keyGenerator.initialize(keySize);

            Provider p = keyGenerator.getProvider();
            System.out.println(p.getName());
            Signature sig = Signature.getInstance(sigAlgName, provider);

            System.out.println("Signature() worked.");

            //Security.addProvider(new BouncyCastleProvider());   


            KeyPair keyPair = keyGenerator.genKeyPair();
            PrivateKey privKey = keyPair.getPrivate();
            PublicKey pubKey = keyPair.getPublic();

            X509Name name = new X509Name(dname);
            DERSet derSet = new DERSet();
            PKCS10CertificationRequest Request =
                new PKCS10CertificationRequest(
                    sigAlgName,
                    name,
                    pubKey,
                    derSet,
                    privKey,
                    provider);

            ByteArrayOutputStream out = new ByteArrayOutputStream();
            byte[] b64data = Base64.encode(Request.getEncoded());
            System.out.println("Request: Length = " + b64data.length);
            out.write(b64data, 0, b64data.length);
            System.out.println(new String(out.toByteArray()));

            ByteArrayInputStream inStream = new ByteArrayInputStream(privKey.getEncoded());
            DERInputStream derInputStream = new DERInputStream(inStream);
            DERObject keyInfo = derInputStream.readObject();
            PrivateKeyInfo pkey = new PrivateKeyInfo((ASN1Sequence)keyInfo);
            DERObject derKey = pkey.getPrivateKey();
            ByteArrayOutputStream bout = new ByteArrayOutputStream();
            DEROutputStream der = new DEROutputStream(bout);
            der.writeObject(derKey);
            byte[] b64privateKey = Base64.encode(bout.toByteArray());
            System.out.println("Request: Length = " + b64privateKey.length);
            out = new ByteArrayOutputStream();
            out.write(b64privateKey, 0, b64privateKey.length);
            System.out.println(new String(out.toByteArray()));
        }
        catch (Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
}