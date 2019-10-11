<img src="https://github.com/billbuchanan/csn09112/blob/master/zadditional/top_csn09112.png"/>
# Diffie-Hellman, Public Key, Private Key and Hashing

In this lab we will investigate key exchange (with DH), some public key encryption and some hash cracking.

Using:

http://asecuritysite.com/encryption/md5

Match the hash signatures with their words (“Falkirk”, “Edinburgh”, “Glasgow” and “Stirling”).

<pre>
03CF54D8CE19777B12732B8C50B3B66F
D586293D554981ED611AB7B01316D2D5
48E935332AADEC763F2C82CDB4601A25
EE19033300A54DF2FA41DB9881B4B723
</pre>

On Kali, for the following /etc/shadow file, determine the matching password:

<pre>
bill:$apr1$waZS/8Tm$jDZmiZBct/c2hysERcZ3m1
mike:$apr1$mKfrJquI$Kx0CL9krmqhCu0SHKqp5Q0
fred:$apr1$Jbe/hCIb$/k3A4kjpJyC06BUUaPRKs0
ian:$apr1$0GyPhsLi$jTTzW0HNS4Cl5ZEoyFLjB.
jane: $1$rqOIRBBN$R2pOQH9egTTVN1Nlst2U7.
</pre>

On Kali, next create a words file (words) with the words of “napier”, “password” “Ankle123” and “inkwell”

Using hashcat crack the following MD5 signatures (hash1):

<pre>
232DD5D7274E0D662F36C575A3BD634C
5F4DCC3B5AA765D61D8327DEB882CF99
6D5875265D1979BDAD1C8A8F383C5FF5
04013F78ACCFEC9B673005FC6F20698D
</pre>

Command used:  hashcat –m 0 hash1 words

Using the method used in the first part of this tutorial, find crack the following for names of fruits (the fruits are all in lowercase):

<pre>
FE01D67A002DFA0F3AC084298142ECCD
1F3870BE274F6C49B3E31A0C6728957F
72B302BF297A228A75730123EFEF7C41
8893DC16B1B2534BAB7B03727145A2BB
889560D93572D538078CE1578567B91A
</pre>

On Kali, and using John the Ripper, and using a word list with the names of fruits, crack the following pwdump passwords:

<pre>
fred:500:E79E56A8E5C6F8FEAAD3B435B51404EE:5EBE7DFA074DA8EE8AEF1FAA2BBDE876:::
bert:501:10EAF413723CBB15AAD3B435B51404EE:CA8E025E9893E8CE3D2CBF847FC56814:::
</pre>

On Kali, and using John the Ripper, the following pwdump passwords (they are names of major Scottish cities/towns):

<pre>
Admin:500:629E2BA1C0338CE0AAD3B435B51404EE:9408CB400B20ABA3DFEC054D2B6EE5A1:::
fred:501:33E58ABB4D723E5EE72C57EF50F76A05:4DFC4E7AA65D71FD4E06D061871C05F2:::
bert:502:BC2B6A869601E4D9AAD3B435B51404EE:2D8947D98F0B09A88DC9FCD6E546A711:::
</pre>

On Kali, and using John the Ripper, crack the following pwdump passwords (they are the names of animals):

<pre>
fred:500:5A8BB08EFF0D416AAAD3B435B51404EE:85A2ED1CA59D0479B1E3406972AB1928:::
bert:501:C6E4266FEBEBD6A8AAD3B435B51404EE:0B9957E8BED733E0350C703AC1CDA822:::
admin:502::333CB006680FAF0A417EAF50CFAC29C3:D2EDBC29463C40E76297119421D2A707:::
</pre>






