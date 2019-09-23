           

<table width="100%" border="1" cellpadding="0" cellspacing="0"> 
<tr><td valign="top">
 <h1 id="logo">Network Security and Cryptography (Software Tut 1)</h1>
<p>This is a basically an introduction to Python coding for network packet capture [<a href="https://github.com/billbuchanan/csn09112/blob/master/week03_ns/labs/lab02_additional.pdf">Lab</a>]. To do the lab you must have WinPCap install [<a href="http://www.winpcap.org/install/default.htm">Download</a>]</p>
    <h2>Number conversions</h2>
    <p>Within cryptography we often have to present numbers in different formating, and typically have to convert from decimal into hexadecimal (based 16). Enter the following Python program:</p>
    <pre>
import sys
val=10

if (len(sys.argv)>1):
	val=int(sys.argv[1])

print "Hex: ",hex(val)
print "Decimal: ",val
print "Octal: ",oct(val)
print "Binary: ",bin(val)
</pre>
<p>Now use it to complete the following table:</p>
<table width="100%">
<tr><td width="25%">Decimal</td><td width="25%">Hex</td><td width="25%">Octal</td><td width="25%">Binary</td></tr>
<tr><td>10</td><td></td><td></td><td></td></tr>
<tr><td></td><td>0x23</td><td></td><td></td></tr>
<tr><td></td><td><td>032</td><td></td></tr>
    <tr><td></td><td><td></td><td>11110001</td></tr>
</table>

</td></tr>
</table>
<h2>WinPCap</h2>
<p>We will use WireShark fairly extensively through the module. <b>The download the WinCap Python script <a href="https://asecuritysite.com/winpcapy.zip">here</a></b>. Put this into the default Python folder (such as c:\python27). Next create the following script [<a href="https://asecuritysite.com/public/dump01.txt">code</a>]:</p>
<pre>
\#\# Based on code at https://code.google.com/p/winpcapy/downloads/detail?name=winpcapy.zip
from ctypes import *
from winpcapy import *
import time
import sys
import string

\# Packet capture function
PHAND=CFUNCTYPE(None,POINTER(c_ubyte),POINTER(pcap_pkthdr),POINTER(c_ubyte))

\#\# Callback function which is called for every new packet
def _packet_handler(param,header,pkt_data):
	local_tv_sec = header.contents.ts.tv_sec
	ltime=time.localtime(local_tv_sec);
	timestr=time.strftime("%H:%M:%S", ltime)
	print
	print("%s,%.6d len:%d" % (timestr, header.contents.ts.tv_usec, header.contents.len))

def get_ad():
	i=0
	d=alldevs.contents
	while d:
		i=i+1
		print("%d. %s" % (i, d.name))
		print (" (%s)\n" % (d.description))
		if d.next:
			d=d.next.contents
		else:
			d=False
	print ("Enter the interface number (1-%d):" % (i))
	inum= raw_input('--> ')
	inum=int(inum)
	d=alldevs
	\#\# Get Selected adaptor
	for i in range(0,inum-1):
		d=d.contents.next
	return d.contents

\#\# Define the Callback function name
packet_handler=PHAND(_packet_handler)

\#\# Find all the devices
alldevs=POINTER(pcap_if_t)()
errbuf= create_string_buffer(PCAP_ERRBUF_SIZE)

if (pcap_findalldevs(byref(alldevs), errbuf) == -1):
	print ("Error in pcap_findalldevs: %s\n" % errbuf.value)
	sys.exit(1)

\#\# Get adapator
d=get_ad()
adhandle = pcap_open_live(d.name,65536,1,1000,errbuf)

print("\nStarting to listen on %s...\n" % (d.description))

\#\# Get 20 packets
pcap_loop(adhandle, 20, packet_handler, None)
pcap_close(adhandle)
</pre>
<p>Run the script. What are the names of your interfaces?</p>
<p>For the first 20 packets, what is the minimum and maximum packet size?</p>
<h2>IP address capture</h2>
<p>Next we will parse the packets for the IP addresses. First add the following to define the parsing of the packets [<a href="https://asecuritysite.com/public/dump02.txt">code</a>]:</p>
<pre>
u_short = c_ushort
u_char = c_ubyte
u_int = c_int

class ip_address(Structure):
    _fields_ = [("byte1", u_char),
                ("byte2", u_char),
                ("byte3", u_char),
                ("byte4", u_char)]

class ip_header(BigEndianStructure):
    _fields_ = [("ver_ihl", u_char),
                ("tos", u_char),
                ("tlen", u_short),
                ("identification", u_short),
                ("flags_fo", u_short),
                ("ttl", u_char),
                ("proto", u_char),
                ("crc", u_short),
                ("saddr", ip_address),
                ("daddr", ip_address),
                ("op_pad", u_int)]
</pre>
<p>Next replace the call back function with:</p>
<pre>
\#\# Callback function which is called for every new packet
def _packet_handler(param,header,pkt_data):

    # retrieve the position of the ip header
	v_pkt_data = ctypes.cast(pkt_data, ctypes.c_void_p)
	v_ip_header = ctypes.c_void_p(v_pkt_data.value + 14)
	pih = ctypes.cast(v_ip_header, ctypes.POINTER(ip_header))
	ih = pih.contents
	print("{}.{}.{}.{} -> {}.{}.{}.{}".format(ih.saddr.byte1, ih.saddr.byte2, ih.saddr.byte3, ih.saddr.byte4, ih.daddr.byte1, ih.daddr.byte2, ih.daddr.byte3, ih.daddr.byte4))
</pre>
<p>Run the code and find the IP address connections for the first five connections?</p>

<h2>Displaying connection details</h2>
<p>Now we will read the TCP header, and which follows the IP address. In this case we will just display the TCP ports. First we add the format of the TCP packet (we have just used the first four fields) [<a href="https://asecuritysite.com/public/dump03.txt">code</a>]:</p>
<pre>
class tcp_header(BigEndianStructure):
    _fields_ = [("source_port", u_short),
                ("destination_port", u_short),
		("seq", u_int),
		("ack", u_int)]
</pre>
<p>And we can replace the call back function:</p>
<pre>
def _packet_handler(param,header,pkt_data):

    # retrieve the position of the ip header
	v_pkt_data = ctypes.cast(pkt_data, ctypes.c_void_p)
	v_ip_header = ctypes.c_void_p(v_pkt_data.value + 14)
	pih = ctypes.cast(v_ip_header, ctypes.POINTER(ip_header))
	ih = pih.contents

 	ip_len = (ih.ver_ihl & 0xf) * 4
	th = ctypes.cast(ctypes.cast(pih, ctypes.c_void_p).value + ip_len,
                     ctypes.POINTER(tcp_header)).contents

	print("{}.{}.{}.{}:{} -> {}.{}.{}.{}:{}".format(ih.saddr.byte1, ih.saddr.byte2, ih.saddr.byte3, ih.saddr.byte4, th.source_port,ih.daddr.byte1, ih.daddr.byte2, ih.daddr.byte3, ih.daddr.byte4,th.destination_port))
</pre>
<h2>Examining the Transport Layer protocol</h2>
<p>The problem with the previous example is that there can be several transport layer protocols. So we must look at the Protocol field in the IP packet. Now modify your packet hander to add the IP Protocol field [<a href="https://asecuritysite.com/public/dump04.txt">Download</a>]:</p>
<pre>
	print("{}.{}.{}.{}:{} -> {}.{}.{}.{}:{} Protocol: {}".format(ih.saddr.byte1, ih.saddr.byte2, ih.saddr.byte3, ih.saddr.byte4, th.source_port,ih.daddr.byte1, ih.daddr.byte2, ih.daddr.byte3, ih.daddr.byte4,th.destination_port,ih.proto))
</pre>
<p>Now run the Python program, and generate some traffic (such as loading a Web page. You will now see other protocols, such as 6- TCP and 17 - UDP. List the protocols that you see:</p>

<p>Run the code and find the IP address connections and TCP ports used for the first five packets?</p>
<h2>Filtering for TCP</h2>
<p>Now we can filter for just TCP traffic by examining the IP Protocol field. For this just replace your packet handler with [<a href="https://asecuritysite.com/public/dump05.txt">code</a>]:</p>
<pre>
def _packet_handler(param,header,pkt_data):
    # retrieve the position of the ip header
	v_pkt_data = ctypes.cast(pkt_data, ctypes.c_void_p)
	v_ip_header = ctypes.c_void_p(v_pkt_data.value + 14)
	pih = ctypes.cast(v_ip_header, ctypes.POINTER(ip_header))
	ih = pih.contents
 	ip_len = (ih.ver_ihl & 0xf) * 4
	th = ctypes.cast(ctypes.cast(pih, ctypes.c_void_p).value + ip_len,
                     ctypes.POINTER(tcp_header)).contents
	if (ih.proto==6):
		print("{}.{}.{}.{}:{} -> {}.{}.{}.{}:{} Protocol: {}".format(ih.saddr.byte1, ih.saddr.byte2, ih.saddr.byte3, ih.saddr.byte4, th.source_port,ih.daddr.byte1, ih.daddr.byte2, ih.daddr.byte3, ih.daddr.byte4,th.destination_port,ih.proto))
</pre>
<p>Next generate some traffic by accessing a Web site (or refreshing the cache). Note the IP addresses and TCP ports of the Web connections:</p>
<p>If you go to https://Google.com, and run your script, which server port is used?</p>
<p>If you go to https://asecuritysite.com, and run your script, which server port is used?</p>
<p>Why do the two sites differ in the server ports?</p>
<h2>Tutorial</h2>
<p>1. Most of the IP packets are IP Version 4. Read the IP Version number from the first four bits with:</p>
<pre>
	ip_ver = (ih.ver_ihl & 0xf0) >> 4
	print "IP Version: ",ip_ver
</pre>
<p>Run the Python program and capture some traffic. Which is the version number defined in the packets, and what does the "& 0xf0" and ">> 4" parts of the code do?</p>

<p>2. In the previous Python program, the TCP fields have not been fully defined. Figure 1 shows the Ethernet, IP and TCP fields. Using the TCP header definition, update the TCP class definition in your Python program to include all of the fields:</p>
<pre>
class tcp_header(BigEndianStructure):
    _fields_ = [("source_port", u_short),
                ("destination_port", u_short),
		("seq", u_int),
		("ack", u_int),
		("flags", u_short),
		("window", u_short),
		("checksum", u_short),
		("urgent", u_short),
		("options", u_int)]
</pre>
<p>Test the output.  Do the SEQ and ACK tie-up on a connection?</p>



<p>2.1 	What values do you get for the Flags field?</p>



<p>2.2	Now mask off the flags with:</p>
<pre>
print " Flags: ",th.flags & 0x0ff,
</pre>	
<p>2.3	What values do you know get? Can you match them to the TCP flags?</p>


<p><img src="https://asecuritysite.com/public/iptcp.png" width="600px" /></p>

<p>3.We will now put the program into an infinite loop and break when there is a keypress. For this we use the Pywin32 library [<a href="http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/pywin32-219.win32-py2.7.exe/download">here</a>], which contains the pyHook class:</p>
<p>Next replace:</p>
<pre>
## Get 20 packets
pcap_loop(adhandle, 20, packet_handler, None)
pcap_close(adhandle)
</pre>
<p>with:</p>
<pre>
import pyHook,pythoncom

def OnKeyboardEvent(event):
	exit()
	pcap_breakloop(ahandle)
	pcap_close(adhandle)

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()

while True:
    try:
	while True:
		pcap_loop(adhandle, 1, packet_handler, None)
        	pythoncom.PumpWaitingMessages()
    except KeyboardInterrupt:
        exit()
</pre>
<p>You should now be able to capture until a key is pressed.</p>
<p>The final solution is [<a href="https://asecuritysite.com/public/dump07.txt">Here</a>]</p>
<h2>Demo</h2>
<p>There is a demo <a href="https://www.youtube.com/watch?v=raphJCH2SPE">here</a></p>
<h2>Note</h2>
<p>In the lecture I say the IP header is 16 bytes, but it is actually 4 times the value in the Header Len of the IP field (which is the first four bits after the IP Version field). So the code:</p>
<pre>
ip_len = (ih.ver_ihl & 0xf) * 4
</pre>
<p>masks off the lower four bits and multiplies by four to get the IP packet header length (and where TCP or UDP header will start).</p>
        </div>

