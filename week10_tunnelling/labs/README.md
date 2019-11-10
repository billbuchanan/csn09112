<img src="https://github.com/billbuchanan/csn09112/blob/master/zadditional/top_csn09112.png"/>

In this lab we will investigate the usage of SSL/TLS and VPN tunnels.

## 1	Web cryptography assessment
The ssllabs tool (https://ssllabs.com) can be used to assess the security of the cryptography used on a Web site. You will be given a range of Web sites to scan in the lab, and you should pick three sites from the list. Now perform a test on them, and determine:

<pre>
What grade does the site get?
			
The digital certificate key size and type?
			
Does the name of the site match the name on the server?			
Who is the signer of the digital certificate?
			
The expiry date on the digital certificate?
			
What is the hashing method on the certificate?
			
If it uses RSA keys, what is the e value that is used in the encryption (Me mod N)?			
Determine a weak cipher suite used and example why it might be weak?
			
What does TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 identify?			
Is SSL v2 supported?

			
If SSL v2 was supported, what problems might there be with the site (this will require some research)?			
Outline the usage of TLS 1.0/1.1 and 1.2, and identify a problem if one of these TLS versions were not supported?			
Is the site vulnerable to Heartbleed?
Is the site vulnerable to DROWN?
Is the site vulnerable to BEAST?
Is the site vulnerable to POODLE?			
</pre>
Research questions:
<pre>
If a site gets a ‘T’ grade, what is the problem?



If the site was susceptible to Poodle, what is the vulnerability?


</pre>


## 2	Viewing details

1	Go to your Kali Linux instance. Run Wireshark and capture traffic from your main network connection. Start a Web browser, and go to www.napier.ac.uk.

<pre>
Stop Wireshark and identify some of your connection details:
	
Your IP address and TCP port:

Napier’s Web server IP address and TCP port:

Right-click on the GET HTTP request from the client, and follow the stream:

What does the red and blue text identify?

Can you read the HTTP requests that go from the client to the server? [Yes][No]
</pre>

2	Go to your Kali Linux instance. Run Wireshark and capture traffic from your main network connection. Start a Web browser, and go to Google.com.

<pre>
Stop Wireshark and identify some of your connection details:
	
Your IP address and TCP port:

Google’s Web server IP address and TCP port:

Which SSL/TLS version is used:

By examining the Wireshark trace, which encryption method is used for the tunnel:

By examining the Wireshark trace, which hash method is used for the tunnel:

By examining the Wireshark trace, what is the length of the encryption key:

By examining the certificate from the browser which encryption method is used for the tunnel:

By examining the certificate from the browser, which hash method is used for the tunnel:

By examining the certificate from the browser is the length of the encryption key:
</pre>


3	Run Wireshark and capture traffic from your main network connection. Start a Web browser, and go to https://twitter.com.

Stop Wireshark and identify some of your connection details:

<pre>
Your IP address and TCP port:

Twitter’s Web server IP address and TCP port:

Which SSL/TLS version is used:

By examining the Wireshark trace, which encryption method is used for the tunnel:

By examining the Wireshark trace, which hash method is used for the tunnel:

By examining the Wireshark trace, what is the length of the encryption key:

By examining the certificate from the browser which encryption method is used for the tunnel:

By examining the certificate from the browser, which hash method is used for the tunnel:

By examining the certificate from the browser is the length of the encryption key:
</pre>

## 3	OpenSSL

1	Go to your Kali Linux instance, and make a connection to the www.live.com Web site:
<pre>
openssl s_client -connect www.live.com:443
</pre>

<pre>
Which SSL/TLS method has been used:

Which method is used on the encryption key on the certificate, and what is the size of the public key?


Which is the handshaking method that has been used to create the encryption key?


Which TLS version is used for the tunnel?


Which encryption method is used for the tunnel:


Which hash method is used for the tunnel:


What is the length of the encryption key:

What is the serial number of the certificate:


Who has signed the certificate:

</pre>

## 4	Examining traces

1	Download the following file, and examine the trace with Wireshark:

http://asecuritysite.com/log/ssl.zip
	
<pre>
Client IP address and TCP port:

Web server IP address and TCP port:

Which SSL/TLS method has been used:

Which encryption method is used for the tunnel:

Which hash method is used for the tunnel:

What is the length of the encryption key:
</pre>


2	Download the following file, and examine the trace with Wireshark:

http://asecuritysite.com/log/https.zip
<pre>
Client IP address and TCP port:

Web server IP address and TCP port:

Which SSL/TLS method has been used:

Which encryption method is used for the tunnel:

Which hash method is used for the tunnel:

What is the length of the encryption key:
</pre>

3	Download the following file, and examine the trace with Wireshark:

http://asecuritysite.com/log/heart.zip	
<pre>
Client IP address and TCP port:

Web server IP address and TCP port:

Which SSL/TLS method has been used:

Which encryption method is used for the tunnel:

Which hash method is used for the tunnel:

What is the length of the encryption key:

Can you spot the packet which identifies the Heartbleed vulnerability?
</pre>

4	Download the following file, and examine the trace with Wireshark:

http://asecuritysite.com/log/ipsec.zip 
<pre>
Which is the IP address of the client and of the server:


Which packet number identifies the start of the VPN connection (Hint: look for UDP Port 500):



Determine one of the encryption and hashing methods that the client wants to use:



Now determine the encryption and hashing methods that are agreed in the ISAKMP:
</pre>




