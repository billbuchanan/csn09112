<img src="https://github.com/billbuchanan/csn09112/blob/master/zadditional/top_csn09112.png"/>

## Introduction

In this lab we will investigate the usage of regular expressions, and using Wireshark filters.

## Detecting content
For Table 1, and using a Wireshark filter, and Table 2, determine the required evidence. An example is:
<pre>
http contains "\x89\x50\x4E\x47"
</pre>


[File 1](http://asecuritysite.com/log/with_png.zip)	Names of PNG files:


[File 2](http://asecuritysite.com/log/with_pdf.zip)	Names of PDF files:


[File 3](http://asecuritysite.com/log/with_gif.zip)
Names of GIF files:


[File 4](http://asecuritysite.com/log/with_jpg.zip)	Names of JPG files:



[File 5](http://asecuritysite.com/log/with_mp3.zip)	Names of MP3 files:


[File 6](http://asecuritysite.com/log/with_rar.zip)	Names of RAR files:


[File 7](http://asecuritysite.com/log/with_avi.zip)	Names of AVI files:


[File 8](http://asecuritysite.com/log/with_gz.zip)	Names of GZ files:


[File 9](http://asecuritysite.com/log/email_cc2.zip)	Email addresses:


[File 10](http://asecuritysite.com/log/email_cc2.zip)	Credit card details:


[File 11](http://asecuritysite.com/log/webpage.zip)	IP address details:


[File 12](http://asecuritysite.com/log/webpage.zip)	Domain name details:



Table 2: Examples of signatures
<pre>
PNG file	"\x89\x50\x4E\x47"
PDF file	"%PDF"
GIF file	"GIF89a"
ZIP file	"\x50\x4B\x03\x04"
JPEG file	"\xff\xd8"
MP3 file	"\x49\x44\x33"
RAR file	"\x52\x61\x72\x21\x1A\x07\x00"
AVI file	"\x52\x49\x46\x46"
SWF file	"\x46\x57\x53"
GZip file	"\x1F\x8B\x08"
Email addresses	 "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]"
IP address	"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}.[0-9]{1,3}"
Credit card details (Mastercard)	"5\d{3}(\s|-)?\d{4}(\s|-)?\d{4}(\s|-)?\d{4}"
Credit card details (Visa):	"4\d{3}(\s|-)?\d{4}(\s|-)?\d{4}(\s|-)?\d{4}"
Credit card details (Am Ex).	"3\d{3}(\s|-)?\d{6}(\s|-)?\d{5}"
Domain name:	"[a-zA-Z0-9\-\.]+\.(com|org|net|mil|edu|COM|ORG|NET|MIL|EDU|UK)"
</pre>

Sample rules:

* PNG Filter: http contains "\x89\x50\x4E\x47"
* PDF Filter: http contains "%PDF"
* GIF Filter: http contains "GIF89a" 
* ZIP Filter: http contains "\x50\x4B\x03\x04".
* JPEG Filter: http contains "\xff\xd8"
* MP3 Filter: http contains "\x49\x44\x33"
* RAR Filter: http contains "\x52\x61\x72\x21\x1A\x07\x00"
* AVI Filter: http contains "\x52\x49\x46\x46"
* SWF Filter: http contains "\x46\x57\x53"
* GZip Filter: http contains "\x1F\x8B\x08"
* Email address Filter: smtp matches ""[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]""
* IP address Filter: http matches ""[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}.[0-9]{1,3}""
* Credit card details (Mastercard) Filter: smtp matches ""5\\d{3}(\\s|-)?\\d{4}(\\s|-)?\\d{4}(\\s|-)?\\d{4}""
* Credit card details (Visa) Filter: smtp matches ""4\\d{3}(\\s|-)?\\d{4}(\\s|-)?\\d{4}(\\s|-)?\\d{4}""
* Credit card details (Am Ex) Filter: smtp matches ""3\\d{3}(\\s|-)?\\d{6}(\\s|-)?\\d{5}""
* Domain name Filter: http matches ""[a-zA-Z0-9\-\.]+\.(com|org|net|mil|edu|COM|ORG|NET|MIL|EDU|UK)""
* FTP User/Password Crack Filter: ftp contains \"530 User\"
* FTP Login Filter: tcp.port==21 && tcp.flags.syn==1 && tcp.flags.ack==1
* Telnet Login Filter: tcp.port==23 && tcp.flags.syn==0 && tcp.flags.ack==0
* Hping DoS Filter: tcp.flags.syn==1 && tcp.flags.ack==0

<img src="https://raw.githubusercontent.com/billbuchanan/csn09112/master/week12_end/labs/wire01.png"/>

### Tshark
We can also process the network traces using Tshark, which is a command line version of Wireshark. For example we can search for a ZIP file with:

<pre>
tshark  -Y "http matches \"\x50\x4B\x03\x04\"" -r with_zip.pcap -x -V > list
</pre>

and then view the list file.

If the path is not setup, you can use:

<pre>
"c:\Program Files\wireshark\tshark.exe" -Y "http matches \"\x50\x4B\x03\x04\"" -r with_zip.pcap -x -V > list
</pre>

Here is a sample run:

<img src="https://raw.githubusercontent.com/billbuchanan/csn09112/master/week12_end/labs/wire01.png"/>

Now repeat some of the example from the first part, and determine some of the details:


[File 1: PNG Content](http://asecuritysite.com/log/with_png.zip)	Frame numbers with content:

IP addresses involved in exchange:

[File 2: PDF Content](http://asecuritysite.com/log/with_pdf.zip)	Frame numbers with content:

IP addresses involved in exchange:

[File 3: GIF Content](http://asecuritysite.com/log/with_gif.zip)
Frame numbers with content:

IP addresses involved in exchange:

[File 4: JPG Content](http://asecuritysite.com/log/with_jpg.zip)	Frame numbers with content:

IP addresses involved in exchange:


## Content identification
There are a number of files contained in this [evidence bag](http://asecuritysite.com/evidence.zip). Using a Hex Editor (such as HxD), see if you can match the magic number, and then change the file extension, and see if you can view them. There is a list of magic numbers [here](http://asecuritysite.com/forensics/magic).

Additional 
## RegEx
Using [Reg101](https://regex101.com), enter the following code:
<pre>
There is not much we can do apart from contacting There is not much we can do apart from contacting f.smith@home.net to see if he would like to reboot the server at 192.168.0.1. If he can do this then I will call him on 444.3212.5431. My credit card details are 4321-4444-5412-2310 and 5430-5411-4333-5123 and my name on the card is Fred Smith. I really like the name domain fred@home. Overall our target areas are SW1 7AF and EH105DT. I tested the server last night, and I think the IP address is 10.0.0.1 and there are two MAC addresses which are  01:23:45:67:89:ab or it might be 00.11.22.33.44.55. 

The book we will use is “At Home” and it can be bought on amazon.com or google.com, if you search for 978-1-4302-1998-9. My password is: 

a1b2c3 

Best regards,

Bert.
EH14 1DJ
+44 (960) 000 00 00
1/1/2009
</pre>

Now, using the Python code generator, create Python code to detect the following:

* Email address.
* MAC address.
* Credit card details.

Some hints are [here](https://asecuritysite.com/dlp/day1)
## Splunk
Using Splunk at http:// asecuritysite.com:8000 determine the following. You will be allocated a login. We can use regular expressions to find information. For example, to find the number of accesses from an IP address which starts with “182.”, we can use:

<pre>
get | regex _raw="182\.\d{1,3}\.\d{1,3}\.\d{1,3}"
</pre>

Determine the number of accesses for GET from any address which begins with 182:


<img src="https://raw.githubusercontent.com/billbuchanan/csn09112/master/week12_end/labs/splunk01.png"/>

The security team search for an address that is ending with .22, and do a search with:
<pre>
get | regex _raw="\d{1,3}.\d{1,3}.\d{1,3}.22"
</pre>

But it picks up logs which do not include addresses with .22 at the end. What is the problem with the request, and how would you modify the request:



You are told that there’s accesses to a file which ends in “a.html”. Using a regular expression, such as:

<pre>
get | regex _raw="[a]+\.html"
</pre>

Outline three HTML files which end with the characters ‘a’, or an ‘e’, and have ‘.html’ as an extension:


A simple domain name check is:
<pre>
get | regex _raw="[a-zA-Z\.]+\.(com|net|uk)"
</pre>

If we now try:

<pre>
get | regex _raw="[a-zA-Z0-9\-\.]+\.(com|org|net|mil|edu|COM|ORG|NET|MIL|EDU|UK)"
</pre>

we will return events with domain names:

Outline which ones have been added:


We can search for email addresses with:

<pre>
get | regex _raw="(?<email>[\w\d\.\-]+\@[\w\d\.]+)"
</pre>

Which email addresses are present:


We can search for times using regular expressions, such as:

<pre>
get | regex _raw="[0-9]{2}\:22\:[0-9]{2}"
</pre>

How many GET requests where there at 22 minutes past the hour:

How many GET requests were made at 14 seconds past the minute:

### NetWitness
Now we will use NetWitness to gather the evidence from the following network traces. To do this, open NetWitness, and start a New Collection. Next select your collection, and Import Packets. After this you can view your evidence, and also perform a File Extract.

Download link: https://asecuritysite.com/public/netwit.zip 

After you examine each one, identify all the IP addresses involved with traces 1 to 8 and any other relevant information that you gain around the location of the host and server:

[File 1](http://asecuritysite.com/log/with_png.zip)	What are the pictures in the trace:


[File 2](http://asecuritysite.com/log/with_pdf.zip)	What does the PDF document contain:


[File 3](http://asecuritysite.com/log/with_gif.zip) What are the pictures in the trace:

[File 4](http://asecuritysite.com/log/with_jpg.zip)	What are the pictures in the trace:

[File 5](http://asecuritysite.com/log/with_mp3.zip)	What are the music files:

[File 6](http://asecuritysite.com/log/with_rar.zip)	What are the contents of the RAR files:

[File 7](http://asecuritysite.com/log/with_avi.zip)	What are the contents of the AVI files:

[File 8](http://asecuritysite.com/log/with_gz.zip) What are the contents for the GZ files:

