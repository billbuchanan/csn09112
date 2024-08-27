## Based on code at https://code.google.com/p/winpcapy/downloads/detail?name=winpcapy.zip
import ctypes
from winpcapy import *
import time
import sys
import string
import pyHook,pythoncom

# Packet capture function
PHAND=CFUNCTYPE(None,POINTER(c_ubyte),POINTER(pcap_pkthdr),POINTER(c_ubyte))

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


class tcp_header(BigEndianStructure):
    _fields_ = [("source_port", u_short),
                ("destination_port", u_short),
		("seq", u_int),
		("ack", u_int),
		("flags", u_short),
		("window", u_short),
		("checksum", u_short),
		("urgent", u_short),
		("options", u_int),

]

## Callback function which is called for every new packet
def _packet_handler(param,header,pkt_data):
	v_pkt_data = ctypes.cast(pkt_data, ctypes.c_void_p)
	v_ip_header = ctypes.c_void_p(v_pkt_data.value + 14)
	pih = ctypes.cast(v_ip_header, ctypes.POINTER(ip_header))
	ih = pih.contents

	ip_len = (ih.ver_ihl & 0xf) * 4
	ip_ver = (ih.ver_ihl & 0xf0) >> 4

	th = ctypes.cast(ctypes.cast(pih, ctypes.c_void_p).value + ip_len,
                     ctypes.POINTER(tcp_header)).contents
	if (ih.proto==6):
		print "IP Version: ",ip_ver,
		print(" TCP: {}.{}.{}.{}:{} -> {}.{}.{}.{}:{}".format(ih.saddr.byte1, ih.saddr.byte2, ih.saddr.byte3, ih.saddr.byte4, th.source_port,ih.daddr.byte1, ih.daddr.byte2, ih.daddr.byte3, ih.daddr.byte4,th.destination_port))
		print " Flags: ",th.flags & 0x0ff,
		print(" Seq: {}, Ack {}".format(hex(th.seq),hex(th.ack)))


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

	## Get Selected adaptor
	for i in range(0,inum-1):
		d=d.contents.next
	return d.contents

## Define the Callback function name
packet_handler=PHAND(_packet_handler)

alldevs=POINTER(pcap_if_t)()
errbuf= create_string_buffer(PCAP_ERRBUF_SIZE)

## Find all the devices
if (pcap_findalldevs(byref(alldevs), errbuf) == -1):
	print ("Error in pcap_findalldevs: %s\n" % errbuf.value)
	sys.exit(1)

## Get adapator
d=get_ad()
adhandle = pcap_open_live(d.name,65536,1,1000,errbuf)

print("\nStarting to listen on %s...\n" % (d.description))


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
 
