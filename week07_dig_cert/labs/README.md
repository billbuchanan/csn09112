<img src="https://github.com/billbuchanan/csn09112/blob/master/zadditional/top_csn09112.png"/>

# Ciphers and Digital Certificates

The aim of this lab is to give an introduction to ciphers, basic encoding/decoding techniques and frequency analysis, as to provide some fundamental understanding. Activities include decoding a range of ciphers and simple calculations. 

4 hours (two supervised hours in the lab, and two additional unsupervised hours).

## Learning activities:
At the end of this lab, you should understand:

* How to decode a range of ciphers.
*	How to recognise certain encodings, such as Base-64, hex, and binary.
*	How to write a Python script to crack PFX certificates. The PKCS#12 (PFX or P12) format is the binary format in which certificates are stored on a server. They are protected by a password and contain the public and private key (the key pair).
*	How to perform bitwise calculations.
*	How to perform frequency analysis.

## Activities
Go to:

http://asecuritysite.com/Challenges

Click on the “Start Challenge” button, and see if you can score over 30 points.

We can also create a short Python script to try to crack the same certificates.

Boot up your Kali VM, and download the following archive: 

http://asecuritysite.com/public/certs.zip

Extract the certificates into the /root folder, and then move into that folder. Now use openssl to try a password:

openssl pkcs12 -nokeys -in bill01.pfx -passin pass:orange

Did you manage to run the script? 

What password is correct for bill01.pfx?

Now implement the Python script in Program 1.

<pre>
from OpenSSL import crypto
words=[]
words.append("coconut")
words.append("mango")
words.append("apples")
words.append("apple")
words.append("oranges")
words.append("orange")
words.append("ankle")
words.append("password")
words.append("bill")
words.append("battery")

for passwd in words:
	try:	
		p12 = crypto.load_pkcs12(open("fredpfx.pfx", 'rb').read(), passwd)
		certificate =p12.get_certificate()
		p12.get_privatekey()      
            print certificate.get_serial_number()
            print certificate.get_issuer().get_components()
            print certificate.get_signature_algorithm()
            print ("Success: "+passwd)
	except Exception as ex:
		print (".")
    </pre>


Can adapt this script to crack some of the other certificates contained in the archive you have downloaded. Bill01.pdf to bill18.pdf are based on fruits (in lowercase), country01.pdf to country06.pdf are based on countries.

Outline the passwords of the certificates:







Can you modify the code so that it shows other details from the certificate, such as its public key,  subject, version and “notBefore”, and “notAfter”.





Ref: https://pyopenssl.org/en/0.15.1/api/crypto.html#x509name-objects









