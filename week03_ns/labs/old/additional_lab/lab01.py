## Based on code at https://code.google.com/p/winpcapy/downloads/detail?name=winpcapy.zip
from ctypes import *
from winpcapy import *
import time
import sys
import string

class timeval(Structure):
    _fields_ = [('tv_sec', c_long),
                ('tv_usec', c_long)]

class pcap_pkthdr(Structure):
    _fields_ = [('ts', timeval),
                ('caplen', bpf_u_int32),
                ('len', bpf_u_int32)]



# Packet capture function
PHAND=CFUNCTYPE(None,POINTER(c_ubyte),POINTER(pcap_pkthdr),POINTER(c_ubyte))

## Callback function which is called for every new packet
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
	inum=input("Enter the interface number (1-%d):" % (i))

	inum=int(inum)
	d=alldevs
	## Get Selected adaptor
	for i in range(0,inum-1):
		d=d.contents.next
	return d.contents

## Define the Callback function name
packet_handler=PHAND(_packet_handler)

## Find all the devices
alldevs=POINTER(pcap_if_t)()
errbuf= create_string_buffer(PCAP_ERRBUF_SIZE)

if (pcap_findalldevs(byref(alldevs), errbuf) == -1):
	print ("Error in pcap_findalldevs: %s\n" % errbuf.value)
	sys.exit(1)

## Get adapator
d=get_ad()
adhandle = pcap_open_live(d.name,65536,1,1000,errbuf)

print("\nStarting to listen on %s...\n" % (d.description))

## Get 20 packets
pcap_loop(adhandle, 20, packet_handler, None)
pcap_close(adhandle)
