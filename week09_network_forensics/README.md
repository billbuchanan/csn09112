<img src="https://github.com/billbuchanan/csn09112/blob/master/zadditional/top_csn09112.png"/>

## Network Forensics
The key objectives of this chapter are:

* Understand some of the methodologies used in network forensics.
* Provide an in-depth understanding of the key network protocols, including IP, TCP, ARP, ICMP, DNS, Application Layer protocols, and so on.
* Define a range of audit sources for network activity.

## Lecture
The main lecture is [here](https://www.youtube.com/watch?v=9_u1eriQtSY).

## Test

The test for this unit is [Test](https://asecuritysite.com/tests/tests?sortBy=sfc09).
## Wireshark Filters
The following uses the Wireshark display filter:
* PNG Filter: http contains "\x89\x50\x4E\x47". Trace with a PNG and PNG filter: [Test](https://asecuritysite.com/forensics/tshark?fname=with_png.pcap&rulesname=http%20contains%20%2289%3A50%3A4E%3A47%22). [Pcap](https://asecuritysite.com/log/with_png.zip).
* PDF Filter: http contains "%PDF". Trace with a PDF and PDF filter: [Test](https://asecuritysite.com/forensics/tshark?fname=with_pdf.pcap&rulesname=http%20contains%20%5C%22%25PDF%5C%22). [Pcap](https://asecuritysite.com/log/with_pdf.zip)
* GIF Filter: http contains "GIF89a". Trace with a GIF and GIF filter: Test. Pcap
* ZIP Filter: http contains "\x50\x4B\x03\x04". Trace with a ZIP and ZIP filter: Test. Pcap
* JPEG Filter: http contains "\xff\xd8". Trace with a JPEG and JPEG filter: Test. Pcap
* MP3 Filter: http contains "\x49\x44\x33". Trace with an MP3 and MP3 filter: Test. Pcap
* RAR Filter: http contains "\x52\x61\x72\x21\x1A\x07\x00". Trace with a RAR and RAR filter: Test. Pcap
* AVI Filter: http contains "\x52\x49\x46\x46". Trace with a AVI and AVI filter: Test. Pcap
* SWF Filter: http contains "\x46\x57\x53". Trace with a SWF and SWF filter: Test. Pcap
* GZip Filter: http contains "\x1F\x8B\x08". Trace with a GZIP and GZIP filter: Test. Pcap
* Email address Filter: smtp matches ""[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]"". Trace with an email and Email regex filter: Test. Pcap
* IP address Filter: http matches ""[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}.[0-9]{1,3}"". Trace with HTTP traffic and IP address regex filter: Test. Pcap
* Credit card details (Mastercard) Filter: smtp matches ""5\\d{3}(\\s|-)?\\d{4}(\\s|-)?\\d{4}(\\s|-)?\\d{4}"". Trace with an email and Mastercard regex filter: Test. Pcap
* Credit card details (Visa) Filter: smtp matches ""4\\d{3}(\\s|-)?\\d{4}(\\s|-)?\\d{4}(\\s|-)?\\d{4}"". Trace with an email and Visa filter regex filter: Test. Pcap
* Credit card details (Am Ex) Filter: smtp matches ""3\\d{3}(\\s|-)?\\d{6}(\\s|-)?\\d{5}"". Trace with an email and Am Ex regex filter: Test. Pcap
* Domain name Filter: http matches ""[a-zA-Z0-9\-\.]+\.(com|org|net|mil|edu|COM|ORG|NET|MIL|EDU|UK)"". Trace with an email and Email regex filter: Test. Pcap
* FTP User/Password Crack Filter: ftp contains \"530 User\". Trace with FTP Hydra and 530 filter: Test. Pcap
* FTP Login Filter: tcp.port==21 && tcp.flags.syn==1 && tcp.flags.ack==1. Trace with FTP Hydra and SYN/Port 21 filter: Test. Pcap
* Telnet Login Filter: tcp.port==23 && tcp.flags.syn==0 && tcp.flags.ack==0. Trace with Telnet Hydra and SYN/Port 23 filter: Test. Pcap
* Hping DoS Filter: tcp.flags.syn==1 && tcp.flags.ack==0. Trace with Hping and SYN flag filter: Test. Pcap

## Network Forensics
The following are some examples of PCAPs:

* Network Forensics - [Ping](https://asecuritysite.com/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Fping.txt)
* Network Forensics - [Telnet](https://asecuritysite.com/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Ftelnet.txt)
* Network Forensics - DNS Lookup
* Network Forensics - FTP
* Network Forensics - NMAP
* Network Forensics - Tracert
* Network Forensics - Web page
* Network Forensics - SSL
* Network Forensics - Spoof Address
* Network Forensics - IPSec
* Network Forensics - GoogleWeb
* Network Forensics - IP Packet (Windows)
* Network Forensics - IP Packet (Ubuntu)
* Network Forensics - Hydra traces: FTP
* Network Forensics - Hydra traces: Telnet
* Network Forensics - Hping traces: hping_fin
* Network Forensics - Hping traces: hping_ping_scan
* Network Forensics - Hping traces: hping_port80
* Network Forensics - Hping traces: hping_port80_fin
* Network Forensics - Hping traces: hping_syn
* Network Forensics - Hping traces: hping_udp_scan
* Network Forensics - Hping traces: hping_udp_scan
* Network Forensics - Hping traces: hydra_ftp
* Network Forensics - Hping traces: hydra_telnet

## Related Material
Some related material:

* Network Forensics - TCPDump This shows an example of analysing simple network traces.
* Tripwire This shows an example of configuring Tripwire in Linux.
* Network Forensics - PCAP analysis

## Slides

The slides for the chapter are [here](https://asecuritysite.com/book_chap08.pdf) and the notes are [here](https://asecuritysite.com/public/unit09.pdf).
