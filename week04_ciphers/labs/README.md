<img src="https://github.com/billbuchanan/csn09112/blob/master/zadditional/top_csn09112.png"/>

# Lab 3: Creating Secure Architectures

## Aim
The aim of this  lab is to build a secure architecture.

## Activities

Complete Lab 3: The lab is [here](https://github.com/billbuchanan/csn09112/blob/master/week04_ciphers/labs/csn09112_lab03.pdf)[<a href="https://www.youtube.com/watch?v=d4a0bDhlyvI" target="_blank">Demo</a>].</p>

## Learning activities
**At the end of this lab**, you should be able to do the following:

* The hosts on your network can connect to each other. Test: Ping from the host in the Private network to the DMZ, and vice-versa.</li>
* You are able to connect to the Internet from a host in the Private network. Test: Open up Google.com from a browser from the host in the Private network</li>
* A host on the DMZ is contactable from outside your network. Test: You either ask someone from another network to ping your host, or you ping from the Public port of the firewall, or you use the host on your public network to ping.</li>
* You are able to discover the range of other firewalls which connect to the network. Test: You use NMAP to scan the 10.221.0.0/24 network, and discover the gateways.</li>
* You are able to perform a scan of the services on a host from another network from your private network. Test: You run NMAP on a server address on another network.</li>


## Lab setup
Our challenge is to setup MyBank Incorp, where each of you will be allocated a network and hosts to configure and get on-line (Figure 1). For this you will be allocated your own network (NET01, NET02, and so on) which you can access from the vSoC Cloud infrastructure (vsoc.napier.ac.uk). You have a pfSense firewall, a Linux host, and a Windows host to achieve your objectives. First log into vSoC (vsoc.napier.ac.uk), and then select your network infrastructure. In this lab we will use Allocation C (10.10.z.z/24).


![Lab](https://github.com/billbuchanan/csn09112/blob/master/zadditional/overview.png)
Figure 1: Lab setup (eth0 – Public, eth1 – Private, eth2 – DMZ)  with 10.10.z.z

## Quick guide</h2>
For Ubtuntu configuration, for 10.10.111.7:

```
sudo ifconfig eth11 10.10.x.7 netmask 255.255.255.0 up 
sudo route add default gw 10.10.x.254
nano /etc/resolve.conf and change "name-server 10.200.3.354"
```

## Your challenges
The main challenges to be solved in this lab are:

* The hosts on your network can connect to each other. **How to test?** Ping from the host in the Private network to the DMZ, and vice-versa. How will I do this? Setup the IP addresses on the hosts to be on the same network as the gateway. The firewall address that the host connects to must be on the same network.	
* You are able to connect to the Internet from a host in the Private network. How to test? Open up Google.com from a browser from the host in the Private network. **How will I do this?** Get your network working, and make sure the domain name service is pointing to 10.221.3.254, and it should work. You may need to debug this. If you can connect to 8.8.8.8, but not the domain name, you have a DNS problem.
	
* A host on the DMZ is contactable from outside your network. **How to test?** You either ask someone from another network to ping your host, or you ping from the Public port of the firewall, or you use the TEST network to ping. **How will I do this?** You setup 1:1 NAT on the host in your DMZ, and map it to an address on the 10.221.0.0/24 network.	

* You are able to discover the range of other firewalls which connect to the network. **How to test?** You use NMAP to scan the 10.221.0.0/24 network, and discover the gateways. **How will I do this?** You should run NMAP from one of the hosts in your network for the 10.221.0.0 network, and that it shows the nodes that are connected (host scan).	

* You are able to perform a scan of the services on a host from another network from your private network. **How to test?** You run NMAP on a server address on another network. **How will I do this?** You should run NMAP to discover the services which are being run on the server in the DMZ on another network.	


## Setting up the network
In this lab we will connect multiple firewalls to the main gateway, and be able to complete the challenges in Table 1. You will be given two things:

Group Number:

Your networks will be: 10.10.x.0/24  192.168.y.0/24  

Demo: https://youtu.be/d4a0bDhlyvI


First log into vSoC (vsoc.napier.ac.uk), and then select your network infrastructure. In this lab we will use Allocation A.
  
![Lab](https://github.com/billbuchanan/csn09112/blob/master/zadditional/overview.png)
Figure 1: Lab setup (eth0 – Public, eth1 – Private, eth2 – DMZ)  with 10.10.z.z

## Initial Firewall Creation
Now go to your folder, and select the firewall for your network. Next configure the Linux server in the Private zone, and the Windows server in the DMZ.

| Perform the following: |
|-------------------------------|
| Boot your firewall, and say no to setting up VLANs.
| Now setup the first three networks adapters with em0 (WAN), em1 (LAN) and em2 (OPT1).
| Check that you have been granted an IP address on the WAN (em0) port. What address is it:
| Can you ping the main gateway from the firewall (10.221.3.254) and your own WAN port?  Yes/No

Now we want to setup your private network gateway.

| Perform the following: |
|-------------------------------|
| Select the (2) option to change the IP addresses on the interfaces. Setup the IP address for the em1 interface to 192.168.x.254/24. 
| Note the URL that you can configure your firewall. What is the URL:

That’s it! You are all finished in doing the initial configuration on the firewall. We will now go ahead and configure the hosts and gain access to the firewall from a Web browser.

## Host setup
Now we will configure the hosts to sit on the Private and DMZ zones.


Setup the Linux host to connect to 10.10.x.7/24 with a default gateway of your firewall port (10.10.x.254/24).

```
sudo ifconfig ethx 10.10.x.7 netmask 255.255.255.0 up
sudo route add default gw 10.10.x.254
```


Next setup the nameserver on the Linux host by editing the /etc/resolv.config and adding a nameserver:

```
sudo nano /etc/resolv.conf
```

then add:
```
nameserver 10.221.3.254
nameserver 8.8.8.8
```

On the Windows server modify the static address on the interface with:

```
IP: 192.168.y.7
Subnet mask: 255.255.255.0
Gateway: 192.168.y.254
DNS: 10.221.3.254
```


Now we will finalise the configuration of the firewall:

Log into the firewall from the Linux host on the Private zone with:

http://10.10.x.254

```
Username: admin, Password: pfsense
```

| Perform the following: |
|-------------------------------|
| Setup the required IP on the DMZ (192.168.y.254) and subnet mask.|
| On the firewall, from Diagnostics, view the ARP cache. Which addresses are in the cache: |
| On the firewall, from Diagnostics, ping each of the 192.168.x.254 and 192.168.x.7 interfaces from the LAN network. Can you ping them? Yes/No |
| On the Windows host, ping 192.168.y.254 and 192.168.y.7 interfaces. Can you ping them? Yes/No Why can’t you ping the 192.168.y.254 interface?|
| On the firewall, create a rule which allows a host on the DMZ to use ICMP to any destination.|
| On the Windows host, ping 192.168.y.254 and 192.168.y.7 interfaces. You should now be able to ping them.|
| On the Windows host, ping 192.168.x.254 and 192.168.x.7 interfaces. You should now be able to ping them.|
| On the firewall, create a rule which allows the Public network to ping both the DMZ and Private network. From the firewall, can you ping the hosts in the DMZ and Private network from the WAN port.|
| Now from the Windows host and the Linux host, ping all the key addresses, including the gateway 10.221.3.254 and 10.200.0.2.|


Now we will investigate NAT on the device.

| Perform the following: |
|-------------------------------|
| Run packet capture on the firewall, and then ping from both the Windows host and the Linux host. Stop the trace.
| Which IP address appears in the pings? 
| Why is it just a single address?

Now we will investigate the routing table on the firewall.

| Perform the following: |
|-------------------------------|
| On the firewall, investigate the firewall, and identify how the device makes decisions on the routing of data packets. What is the default gateway?



## D	Device Audit
Now we will make sure everything is in order with our infrastructure, such as for testing for network traffic, MAC addresses and so on. Audit list:

| Perform and answer the following: |
|-------------------------------|
| On the firewall, capture traffic on the DMZ port, and generate some traffic from the LAN to the DMZ (such as accessing the Web server in the DMZ).  Does the traffic have the IP address of the gateway on the LAN port? Tick [ ]
| On the firewall, capture traffic on the WAN port, and generate some traffic from the LAN and DMZ (such as accessing Google.com).  Does the traffic have the IP address of the WAN port? Tick [ ]
| On the firewall, examine the ARP table. Also on the hosts in the DMZ and the LAN, run arp –a, and determine all your MAC addresses.  Do all the MAC addresses tie-up? Tick [ ]

## E	NMAP
Run Wireshark on both hosts. Now run NMAP from the Linux host to the Windows host, and from the Windows host to the Linux host.

| Perform and answer the following: |
|-------------------------------|
| What IP addresses are used in the source addresses of the scan?
| Which services have been identified from the Linux host to the Windows host?
| Which services have been identified from the Windows host to the Linux host?
| Why are these different in their scope? Where is the blocking happening?



Now enable http, https, and ftp from the Private network to the DMZ.
Now enable https, https, and ftp from the DMZ to the Private network.

| Perform and answer the following: |
|-------------------------------|
| Re-do NMAP. How are the scans different?
| Can you now access the Web server from the Linux host to the Windows host?
| Can you now access the Web server from the Windows host to the Linux host?


Access Google.com from the Linux host.

| Perform and answer the following: |
|-------------------------------|
| Can you access it? If not, on the firewall, enable UDP/TCP DNS (Port 53) from DMZ and also from the Private network. Add logging on the rule.
| Can you now access Google.com from the Linux host and the Windows host?
| On the firewall, examine the log and view the accesses for a DNS lookup on Google.com. Which addresses are present?



## F Identifying Services 
Within a network infrastructure we have services which run on hosts. These services provide a given functionality, such as for sending/receiving email, file storage, and so on.

| From → To |	Command	| Observation |
|------|------------|-------------|
| DMZ	| On your Windows host, run the command: netstat –a and outline some of the services which are running on your host (define the port number and the name of the service and only pick off the LISTENING status on the port).	| Outline some of the services which are running on your host (define the port number and the name of the service): |
| LAN		| For the Ubuntu Virtual Machine, and run the command: netstat –l.  	| 	Outline some of the services which are running on your host (define the port number and the name of the service):	| 
| DMZ		| Next we will determine if these services are working. There should be a Web server working on each of the virtual machines (Ubuntu and Windows 2003), so from the Windows host and using a Web browser, access the home page: http://10.10.x.7		|  Is the service working: [Yes] [No] 	| 
|  LAN	|  From Ubuntu, access the Web server at: http://10.10.y.7	| Is the service working: [Yes] [No]| 
| LAN	|  Next we will determine if these services are working using a command line. From your UBUNTU host, undertake the following: telnet 10.10.y.7 80
then enter:  GET / | 	Outline the message that is returned: | 
| DMZ	|  Repeat the previous example from the WINDOWS host: telnet 10.10.x.7 80	|  
| DMZ	|  There should be an FTP server working on Ubuntu and Windows 2003. From WINDOWS, access the FTP server on the UBUNTU server: telnet 10.10.x.7 21
then enter: USER napier PASS napier123 QUIT | 	Outline the messages that you received: What happens to each of these when you try with an incorrect username and password:  | 
| LAN | 	From UBUNTU access the WINDOWS host with telnet 10.10.x.7 21 then enter: USER Administrator PASS napier QUIT | 	Outline the messages that you received: What happens to each of these when you try with an incorrect username and password: | 
| DMZ	| On the UBUNTU instance you will see that the VNC service is running, which is the remote access service. From your WINDOWS host, access the VNC service using a VNC client, and see what happens. |  What does this service do: | 
|  DMZ	| Next we will assess the SMTP service running on the WINDOWS virtual machine. From your UBUNTU machine console run a service to access SMTP:
telnet 10.10.y.7 25 Table 1 outlines the commands to use. 	On the WINDOWS virtual machine, go into the C:\inetpub\mailroot\queue folder, and view the queued email message.  | Was the mail successfully queued? If not, which mail folder has the file in? Outline the format of the EML file?


Table 1: SMTP commands
```
220 napier Microsoft ESMTP MAIL Service, Version: 6.0.3790.3959 ready at  Sun, 2 Dec 2009 21:56:01 +0000
help
214-This server supports the following commands:
214 HELO EHLO STARTTLS RCPT DATA RSET MAIL QUIT HELP AUTH TURN ETRN BDAT VRFY
helo me
250 napier Hello [10.10.75.1]
mail from: email@domain.com
250 2.1.0 email@domain.com....Sender OK
rcpt to: fred@mydomain.com
250 2.1.5 fred@mydomain.com
Data
354 Start mail input; end with <CRLF>.<CRLF>
From: Bob <bob@test.org>
To: Alice <alice@test.org >
Date: Sun, 20 Dec 2013
Subject: Test message
Hello Alice.
This is an email to say hello
.
250 2.6.0 <NAPIERMp7lzvxrMVHFb00000001@napier> Queued mail for delivery
```

## G	Enumeration – Host scan 

Nmap is one of the most popular network scanning tools. It is widely available, for Windows and Linux/Unix platforms, and has both a Command Line Interface (CLI) and a Graphical User Interface (GUI).  

| From → To |	Command	| Observation |
|------|------------|-------------|
| LAN to WAN|	sudo nmap –sP –r 10.221.0.0/24	|Which hosts are on-line:| 

| LAN to DMZ|	sudo nmap –sP –r 10.10.y.0/24|	Which hosts are on-line:| 

| DMZ to LAN	|nmap –sP –r 10.10.x.0/24|	Which hosts are on-line:| 
| LAN to DMZ|	Run Wireshark on host in LAN, and run: sudo nmap –sP –r 10.10.y.0/24|	Which transport layer protocol does NMAP use to discover the host: [ICMP] or [ARP]| 
| LAN to LAN	Run Wireshark on host in LAN, and run: sudo nmap –sP –r 10.10.x.0/24|	Which transport layer protocol does NMAP use to discover the host: [ICMP] or [ARP]| 




## IP Allocation

### Allocation A
```
Allocated	Ubuntu	        	Windows	        Em0	    Em1 (Private)	    Em2 (DMZ)
----------------------------------------------------------------------------------------
Group_001	192.168.1.7/24		192.168.2.7/24	DHCP	192.168.1.254/24	192.168.2.254/24
Group_002	192.168.3.7/24		192.168.4.7/24	DHCP	192.168.3.254/24	192.168.4.254/24
Group_003	192.168.5.7/24		192.168.6.7/24	DHCP	192.168.5.254/24	192.168.6.254/24
Group_004	192.168.7.7/24		192.168.8.7/24	DHCP	192.168.7.254/24	192.168.8.254/24
Group_005	192.168.9.7/24		192.168.10.7/24	DHCP	192.168.9.254/24	192.168.10.254/24
Group_006	192.168.11.7/24		192.168.12.7/24	DHCP	192.168.11.254/24	192.168.12.254/24
Group_007	192.168.13.7/24		192.168.14.7/24	DHCP	192.168.13.254/24	192.168.14.254/24
Group_008	192.168.15.7/24		192.168.16.7/24	DHCP	192.168.15.254/24	192.168.16.254/24
Group_009	192.168.17.7/24		192.168.18.7/24	DHCP	192.168.17.254/24	192.168.18.254/24
Group_010	192.168.19.7/24		192.168.20.7/24	DHCP	192.168.19.254/24	192.168.20.254/24
Group_011	192.168.21.7/24		192.168.22.7/24	DHCP	192.168.21.254/24	192.168.22.254/24
Group_012	192.168.23.7/24		192.168.24.7/24	DHCP	192.168.23.254/24	192.168.24.254/24
Group_013	192.168.25.7/24		192.168.26.7/24	DHCP	192.168.25.254/24	192.168.26.254/24
Group_014	192.168.27.7/24		192.168.28.7/24	DHCP	192.168.27.254/24	192.168.28.254/24
Group_015	192.168.29.7/24		192.168.30.7/24	DHCP	192.168.29.254/24	192.168.30.254/24
Group_016	192.168.31.7/24		192.168.32.7/24	DHCP	192.168.31.254/24	192.168.32.254/24
Group_017	192.168.33.7/24		192.168.34.7/24	DHCP	192.168.33.254/24	192.168.34.254/24
Group_018	192.168.35.7/24		192.168.36.7/24	DHCP	192.168.35.254/24	192.168.36.254/24
Group_019	192.168.37.7/24		192.168.38.7/24	DHCP	192.168.37.254/24	192.168.38.254/24
Group_020	192.168.39.7/24		192.168.40.7/24	DHCP	192.168.39.254/24	192.168.40.254/24
Group_021	192.168.41.7/24		192.168.42.7/24	DHCP	192.168.41.254/24	192.168.42.254/24
Group_022	192.168.43.7/24		192.168.44.7/24	DHCP	192.168.43.254/24	192.168.44.254/24
Group_023	192.168.45.7/24		192.168.46.7/24	DHCP	192.168.45.254/24	192.168.46.254/24
Group_024	192.168.47.7/24		192.168.48.7/24	DHCP	192.168.47.254/24	192.168.48.254/24
Group_025	192.168.49.7/24		192.168.50.7/24	DHCP	192.168.49.254/24	192.168.50.254/24
Group_026	192.168.51.7/24		192.168.52.7/24	DHCP	192.168.51.254/24	192.168.52.254/24
Group_027	192.168.53.7/24		192.168.54.7/24	DHCP	192.168.53.254/24	192.168.54.254/24
Group_028	192.168.55.7/24		192.168.56.7/24	DHCP	192.168.55.254/24	192.168.56.254/24
Group_029	192.168.57.7/24		192.168.58.7/24	DHCP	192.168.57.254/24	192.168.58.254/24
Group_030	192.168.59.7/24		192.168.60.7/24	DHCP	192.168.59.254/24	192.168.60.254/24
Group_031	192.168.61.7/24		192.168.62.7/24	DHCP	192.168.61.254/24	192.168.62.254/24
Group_032	192.168.63.7/24		192.168.64.7/24	DHCP	192.168.63.254/24	192.168.64.254/24
Group_033	192.168.65.7/24		192.168.66.7/24	DHCP	192.168.65.254/24	192.168.66.254/24
Group_034	192.168.67.7/24		192.168.68.7/24	DHCP	192.168.67.254/24	192.168.68.254/24
Group_035	192.168.69.7/24		192.168.70.7/24	DHCP	192.168.69.254/24	192.168.70.254/24
Group_036	192.168.71.7/24		192.168.72.7/24	DHCP	192.168.71.254/24	192.168.72.254/24
Group_037	192.168.73.7/24		192.168.74.7/24	DHCP	192.168.73.254/24	192.168.74.254/24
Group_038	192.168.75.7/24		192.168.76.7/24	DHCP	192.168.75.254/24	192.168.76.254/24
Group_039	192.168.77.7/24		192.168.78.7/24	DHCP	192.168.77.254/24	192.168.78.254/24
Group_040	192.168.79.7/24		192.168.80.7/24	DHCP	192.168.79.254/24	192.168.80.254/24
Group_041	192.168.81.7/24		192.168.82.7/24	DHCP	192.168.81.254/24	192.168.82.254/24
Group_042	192.168.83.7/24		192.168.84.7/24	DHCP	192.168.83.254/24	192.168.84.254/24
Group_043	192.168.85.7/24		192.168.86.7/24	DHCP	192.168.85.254/24	192.168.86.254/24
Group_044	192.168.87.7/24		192.168.88.7/24	DHCP	192.168.87.254/24	192.168.88.254/24
Group_045	192.168.89.7/24		192.168.90.7/24	DHCP	192.168.89.254/24	192.168.90.254/24
Group_046	192.168.91.7/24		192.168.92.7/24	DHCP	192.168.91.254/24	192.168.92.254/24
Group_047	192.168.93.7/24		192.168.94.7/24	DHCP	192.168.93.254/24	192.168.94.254/24
Group_048	192.168.95.7/24		192.168.96.7/24	DHCP	192.168.95.254/24	192.168.96.254/24
Group_049	192.168.97.7/24		192.168.98.7/24	DHCP	192.168.97.254/24	192.168.98.254/24
Group_050	192.168.99.7/24		192.168.100.7/24 DHCP	192.168.99.254/24	192.168.100.254/24
Group_051	192.168.101.7/24	192.168.102.7/24 DHCP	192.168.101.254/24	192.168.102.254/24
Group_052	192.168.103.7/24	192.168.104.7/24 DHCP	192.168.103.254/24	192.168.104.254/24
Group_053	192.168.105.7/24	192.168.106.7/24 DHCP	192.168.105.254/24	192.168.106.254/24
Group_054	192.168.107.7/24	192.168.108.7/24 DHCP	192.168.107.254/24	192.168.108.254/24
Group_055	192.168.109.7/24	192.168.110.7/24 DHCP	192.168.109.254/24	192.168.110.254/24
Group_056	192.168.111.7/24	192.168.112.7/24 DHCP	192.168.111.254/24	192.168.112.254/24
Group_057	192.168.113.7/24	192.168.114.7/24 DHCP	192.168.113.254/24	192.168.114.254/24
Group_058	192.168.115.7/24	192.168.116.7/24 DHCP	192.168.115.254/24	192.168.116.254/24
Group_059	192.168.117.7/24	192.168.118.7/24 DHCP	192.168.117.254/24	192.168.118.254/24
Group_060	192.168.119.7/24	192.168.120.7/24 DHCP	192.168.119.254/24	192.168.120.254/24
Group_061	192.168.121.7/24	192.168.122.7/24 DHCP	192.168.121.254/24	192.168.122.254/24
Group_062	192.168.123.7/24	192.168.124.7/24 DHCP	192.168.123.254/24	192.168.124.254/24
Group_063	192.168.125.7/24	192.168.126.7/24 DHCP	192.168.125.254/24	192.168.126.254/24
Group_064	192.168.127.7/24	192.168.128.7/24 DHCP	192.168.127.254/24	192.168.128.254/24
Group_065	192.168.129.7/24	192.168.130.7/24 DHCP	192.168.129.254/24	192.168.130.254/24
Group_066	192.168.131.7/24	192.168.132.7/24 DHCP	192.168.131.254/24	192.168.132.254/24
Group_067	192.168.133.7/24	192.168.134.7/24 DHCP	192.168.133.254/24	192.168.134.254/24
Group_068	192.168.135.7/24	192.168.136.7/24 DHCP	192.168.135.254/24	192.168.136.254/24
Group_069	192.168.137.7/24	192.168.138.7/24 DHCP	192.168.137.254/24	192.168.138.254/24
Group_070	192.168.139.7/24	192.168.140.7/24 DHCP	192.168.139.254/24	192.168.140.254/24
Group_071	192.168.141.7/24	192.168.142.7/24 DHCP	192.168.141.254/24	192.168.142.254/24
Group_072	192.168.143.7/24	192.168.144.7/24 DHCP	192.168.143.254/24	192.168.144.254/24
Group_073	192.168.145.7/24	192.168.146.7/24 DHCP	192.168.145.254/24	192.168.146.254/24
Group_074	192.168.147.7/24	192.168.148.7/24 DHCP	192.168.147.254/24	192.168.148.254/24
Group_075	192.168.149.7/24	192.168.150.7/24 DHCP	192.168.149.254/24	192.168.150.254/24
Group_075	192.168.151.7/24	192.168.152.7/24 DHCP	192.168.151.254/24	192.168.152.254/24
Group_077	192.168.153.7/24	192.168.154.7/24 DHCP	192.168.153.254/24	192.168.154.254/24
Group_078	192.168.155.7/24	192.168.156.7/24 DHCP	192.168.155.254/24	192.168.156.254/24
Group_079	192.168.157.7/24	192.168.158.7/24 DHCP	192.168.157.254/24	192.168.158.254/24
Group_080	192.168.159.7/24	192.168.160.7/24 DHCP	192.168.159.254/24	192.168.160.254/24
Group_081	192.168.161.7/24	192.168.162.7/24 DHCP	192.168.161.254/24	192.168.162.254/24
Group_082	192.168.163.7/24	192.168.164.7/24 DHCP	192.168.163.254/24	192.168.164.254/24
Group_083	192.168.165.7/24	192.168.166.7/24 DHCP	192.168.165.254/24	192.168.166.254/24
Group_084	192.168.167.7/24	192.168.168.7/24 DHCP	192.168.167.254/24	192.168.168.254/24
Group_085	192.168.169.7/24	192.168.170.7/24 DHCP	192.168.169.254/24	192.168.170.254/24
Group_086	192.168.171.7/24	192.168.172.7/24 DHCP	192.168.171.254/24	192.168.172.254/24
Group_087	192.168.173.7/24	192.168.174.7/24 DHCP	192.168.173.254/24	192.168.174.254/24
```

### Allocation B
```
Allocated	Ubuntu	        Windows	        Em0	    Em1 (Private)	    Em2 (DMZ)
----------------------------------------------------------------------------------------
Group_001	172.16.1.7/24		172.16.2.7/24	DHCP	172.16.1.254/24	172.16.2.254/24
Group_002	172.16.3.7/24		172.16.4.7/24	DHCP	172.16.3.254/24	172.16.4.254/24
Group_003	172.16.5.7/24		172.16.6.7/24	DHCP	172.16.5.254/24	172.16.6.254/24
Group_004	172.16.7.7/24		172.16.8.7/24	DHCP	172.16.7.254/24	172.16.8.254/24
Group_005	172.16.9.7/24		172.16.10.7/24	DHCP	172.16.9.254/24	172.16.10.254/24
Group_006	172.16.11.7/24		172.16.12.7/24	DHCP	172.16.11.254/24	172.16.12.254/24
Group_007	172.16.13.7/24		172.16.14.7/24	DHCP	172.16.13.254/24	172.16.14.254/24
Group_008	172.16.15.7/24		172.16.16.7/24	DHCP	172.16.15.254/24	172.16.16.254/24
Group_009	172.16.17.7/24		172.16.18.7/24	DHCP	172.16.17.254/24	172.16.18.254/24
Group_010	172.16.19.7/24		172.16.20.7/24	DHCP	172.16.19.254/24	172.16.20.254/24
Group_011	172.16.21.7/24		172.16.22.7/24	DHCP	172.16.21.254/24	172.16.22.254/24
Group_012	172.16.23.7/24		172.16.24.7/24	DHCP	172.16.23.254/24	172.16.24.254/24
Group_013	172.16.25.7/24		172.16.26.7/24	DHCP	172.16.25.254/24	172.16.26.254/24
Group_014	172.16.27.7/24		172.16.28.7/24	DHCP	172.16.27.254/24	172.16.28.254/24
Group_015	172.16.29.7/24		172.16.30.7/24	DHCP	172.16.29.254/24	172.16.30.254/24
Group_016	172.16.31.7/24		172.16.32.7/24	DHCP	172.16.31.254/24	172.16.32.254/24
Group_017	172.16.33.7/24		172.16.34.7/24	DHCP	172.16.33.254/24	172.16.34.254/24
Group_018	172.16.35.7/24		172.16.36.7/24	DHCP	172.16.35.254/24	172.16.36.254/24
Group_019	172.16.37.7/24		172.16.38.7/24	DHCP	172.16.37.254/24	172.16.38.254/24
Group_020	172.16.39.7/24		172.16.40.7/24	DHCP	172.16.39.254/24	172.16.40.254/24
Group_021	172.16.41.7/24		172.16.42.7/24	DHCP	172.16.41.254/24	172.16.42.254/24
Group_022	172.16.43.7/24		172.16.44.7/24	DHCP	172.16.43.254/24	172.16.44.254/24
Group_023	172.16.45.7/24		172.16.46.7/24	DHCP	172.16.45.254/24	172.16.46.254/24
Group_024	172.16.47.7/24		172.16.48.7/24	DHCP	172.16.47.254/24	172.16.48.254/24
Group_025	172.16.49.7/24		172.16.50.7/24	DHCP	172.16.49.254/24	172.16.50.254/24
Group_026	172.16.51.7/24		172.16.52.7/24	DHCP	172.16.51.254/24	172.16.52.254/24
Group_027	172.16.53.7/24		172.16.54.7/24	DHCP	172.16.53.254/24	172.16.54.254/24
Group_028	172.16.55.7/24		172.16.56.7/24	DHCP	172.16.55.254/24	172.16.56.254/24
Group_029	172.16.57.7/24		172.16.58.7/24	DHCP	172.16.57.254/24	172.16.58.254/24
Group_030	172.16.59.7/24		172.16.60.7/24	DHCP	172.16.59.254/24	172.16.60.254/24
Group_031	172.16.61.7/24		172.16.62.7/24	DHCP	172.16.61.254/24	172.16.62.254/24
Group_032	172.16.63.7/24		172.16.64.7/24	DHCP	172.16.63.254/24	172.16.64.254/24
Group_033	172.16.65.7/24		172.16.66.7/24	DHCP	172.16.65.254/24	172.16.66.254/24
Group_034	172.16.67.7/24		172.16.68.7/24	DHCP	172.16.67.254/24	172.16.68.254/24
Group_035	172.16.69.7/24		172.16.70.7/24	DHCP	172.16.69.254/24	172.16.70.254/24
Group_036	172.16.71.7/24		172.16.72.7/24	DHCP	172.16.71.254/24	172.16.72.254/24
Group_037	172.16.73.7/24		172.16.74.7/24	DHCP	172.16.73.254/24	172.16.74.254/24
Group_038	172.16.75.7/24		172.16.76.7/24	DHCP	172.16.75.254/24	172.16.76.254/24
Group_039	172.16.77.7/24		172.16.78.7/24	DHCP	172.16.77.254/24	172.16.78.254/24
Group_040	172.16.79.7/24		172.16.80.7/24	DHCP	172.16.79.254/24	172.16.80.254/24
Group_041	172.16.81.7/24		172.16.82.7/24	DHCP	172.16.81.254/24	172.16.82.254/24
Group_042	172.16.83.7/24		172.16.84.7/24	DHCP	172.16.83.254/24	172.16.84.254/24
Group_043	172.16.85.7/24		172.16.86.7/24	DHCP	172.16.85.254/24	172.16.86.254/24
Group_044	172.16.87.7/24		172.16.88.7/24	DHCP	172.16.87.254/24	172.16.88.254/24
Group_045	172.16.89.7/24		172.16.90.7/24	DHCP	172.16.89.254/24	172.16.90.254/24
Group_046	172.16.91.7/24		172.16.92.7/24	DHCP	172.16.91.254/24	172.16.92.254/24
Group_047	172.16.93.7/24		172.16.94.7/24	DHCP	172.16.93.254/24	172.16.94.254/24
Group_048	172.16.95.7/24		172.16.96.7/24	DHCP	172.16.95.254/24	172.16.96.254/24
Group_049	172.16.97.7/24		172.16.98.7/24	DHCP	172.16.97.254/24	172.16.98.254/24
Group_050	172.16.99.7/24		172.16.100.7/24 DHCP	172.16.99.254/24	172.16.100.254/24
Group_051	172.16.101.7/24	172.16.102.7/24 DHCP	172.16.101.254/24	172.16.102.254/24
Group_052	172.16.103.7/24	172.16.104.7/24 DHCP	172.16.103.254/24	172.16.104.254/24
Group_053	172.16.105.7/24	172.16.106.7/24 DHCP	172.16.105.254/24	172.16.106.254/24
Group_054	172.16.107.7/24	172.16.108.7/24 DHCP	172.16.107.254/24	172.16.108.254/24
Group_055	172.16.109.7/24	172.16.110.7/24 DHCP	172.16.109.254/24	172.16.110.254/24
Group_056	172.16.111.7/24	172.16.112.7/24 DHCP	172.16.111.254/24	172.16.112.254/24
Group_057	172.16.113.7/24	172.16.114.7/24 DHCP	172.16.113.254/24	172.16.114.254/24
Group_058	172.16.115.7/24	172.16.116.7/24 DHCP	172.16.115.254/24	172.16.116.254/24
Group_059	172.16.117.7/24	172.16.118.7/24 DHCP	172.16.117.254/24	172.16.118.254/24
Group_060	172.16.119.7/24	172.16.120.7/24 DHCP	172.16.119.254/24	172.16.120.254/24
Group_061	172.16.121.7/24	172.16.122.7/24 DHCP	172.16.121.254/24	172.16.122.254/24
Group_062	172.16.123.7/24	172.16.124.7/24 DHCP	172.16.123.254/24	172.16.124.254/24
Group_063	172.16.125.7/24	172.16.126.7/24 DHCP	172.16.125.254/24	172.16.126.254/24
Group_064	172.16.127.7/24	172.16.128.7/24 DHCP	172.16.127.254/24	172.16.128.254/24
Group_065	172.16.129.7/24	172.16.130.7/24 DHCP	172.16.129.254/24	172.16.130.254/24
Group_066	172.16.131.7/24	172.16.132.7/24 DHCP	172.16.131.254/24	172.16.132.254/24
Group_067	172.16.133.7/24	172.16.134.7/24 DHCP	172.16.133.254/24	172.16.134.254/24
Group_068	172.16.135.7/24	172.16.136.7/24 DHCP	172.16.135.254/24	172.16.136.254/24
Group_069	172.16.137.7/24	172.16.138.7/24 DHCP	172.16.137.254/24	172.16.138.254/24
Group_070	172.16.139.7/24	172.16.140.7/24 DHCP	172.16.139.254/24	172.16.140.254/24
Group_071	172.16.141.7/24	172.16.142.7/24 DHCP	172.16.141.254/24	172.16.142.254/24
Group_072	172.16.143.7/24	172.16.144.7/24 DHCP	172.16.143.254/24	172.16.144.254/24
Group_073	172.16.145.7/24	172.16.146.7/24 DHCP	172.16.145.254/24	172.16.146.254/24
Group_074	172.16.147.7/24	172.16.148.7/24 DHCP	172.16.147.254/24	172.16.148.254/24
Group_075	172.16.149.7/24	172.16.150.7/24 DHCP	172.16.149.254/24	172.16.150.254/24
Group_075	172.16.151.7/24	172.16.152.7/24 DHCP	172.16.151.254/24	172.16.152.254/24
Group_077	172.16.153.7/24	172.16.154.7/24 DHCP	172.16.153.254/24	172.16.154.254/24
Group_078	172.16.155.7/24	172.16.156.7/24 DHCP	172.16.155.254/24	172.16.156.254/24
Group_079	172.16.157.7/24	172.16.158.7/24 DHCP	172.16.157.254/24	172.16.158.254/24
Group_080	172.16.159.7/24	172.16.160.7/24 DHCP	172.16.159.254/24	172.16.160.254/24
Group_081	172.16.161.7/24	172.16.162.7/24 DHCP	172.16.161.254/24	172.16.162.254/24
Group_082	172.16.163.7/24	172.16.164.7/24 DHCP	172.16.163.254/24	172.16.164.254/24
Group_083	172.16.165.7/24	172.16.166.7/24 DHCP	172.16.165.254/24	172.16.166.254/24
Group_084	172.16.167.7/24	172.16.168.7/24 DHCP	172.16.167.254/24	172.16.168.254/24
Group_085	172.16.169.7/24	172.16.170.7/24 DHCP	172.16.169.254/24	172.16.170.254/24
Group_086	172.16.171.7/24	172.16.172.7/24 DHCP	172.16.171.254/24	172.16.172.254/24
Group_087	172.16.173.7/24	172.16.174.7/24 DHCP	172.16.173.254/24	172.16.174.254/24
```

### Allocation C
```
Allocated	Ubuntu	        Windows	        Em0	    Em1 (Private)	Em2 (DMZ)
-----------------------------------------------------------------------------------
Group_001	10.10.1.7/24	10.10.2.7/24	DHCP	10.10.1.254/24	10.10.2.254/24
Group_002	10.10.3.7/24	10.10.4.7/24	DHCP	10.10.3.254/24	10.10.4.254/24
Group_003	10.10.5.7/24	10.10.6.7/24	DHCP	10.10.5.254/24	10.10.6.254/24
Group_004	10.10.7.7/24	10.10.8.7/24	DHCP	10.10.7.254/24	10.10.8.254/24
Group_005	10.10.9.7/24	10.10.10.7/24	DHCP	10.10.9.254/24	10.10.10.254/24
Group_006	10.10.11.7/24	10.10.12.7/24	DHCP	10.10.11.254/24	10.10.12.254/24
Group_007	10.10.13.7/24	10.10.14.7/24	DHCP	10.10.13.254/24	10.10.14.254/24
Group_008	10.10.15.7/24	10.10.16.7/24	DHCP	10.10.15.254/24	10.10.16.254/24
Group_009	10.10.17.7/24	10.10.18.7/24	DHCP	10.10.17.254/24	10.10.18.254/24
Group_010	10.10.19.7/24	10.10.20.7/24	DHCP	10.10.19.254/24	10.10.20.254/24
Group_011	10.10.21.7/24	10.10.22.7/24	DHCP	10.10.21.254/24	10.10.22.254/24
Group_012	10.10.23.7/24	10.10.24.7/24	DHCP	10.10.23.254/24	10.10.24.254/24
Group_013	10.10.25.7/24	10.10.26.7/24	DHCP	10.10.25.254/24	10.10.26.254/24
Group_014	10.10.27.7/24	10.10.28.7/24	DHCP	10.10.27.254/24	10.10.28.254/24
Group_015	10.10.29.7/24	10.10.30.7/24	DHCP	10.10.29.254/24	10.10.30.254/24
Group_016	10.10.31.7/24	10.10.32.7/24	DHCP	10.10.31.254/24	10.10.32.254/24
Group_017	10.10.33.7/24	10.10.34.7/24	DHCP	10.10.33.254/24	10.10.34.254/24
Group_018	10.10.35.7/24	10.10.36.7/24	DHCP	10.10.35.254/24	10.10.36.254/24
Group_019	10.10.37.7/24	10.10.38.7/24	DHCP	10.10.37.254/24	10.10.38.254/24
Group_020	10.10.39.7/24	10.10.40.7/24	DHCP	10.10.39.254/24	10.10.40.254/24
Group_021	10.10.41.7/24	10.10.42.7/24	DHCP	10.10.41.254/24	10.10.42.254/24
Group_022	10.10.43.7/24	10.10.44.7/24	DHCP	10.10.43.254/24	10.10.44.254/24
Group_023	10.10.45.7/24	10.10.46.7/24	DHCP	10.10.45.254/24	10.10.46.254/24
Group_024	10.10.47.7/24	10.10.48.7/24	DHCP	10.10.47.254/24	10.10.48.254/24
Group_025	10.10.49.7/24	10.10.50.7/24	DHCP	10.10.49.254/24	10.10.50.254/24
Group_026	10.10.51.7/24	10.10.52.7/24	DHCP	10.10.51.254/24	10.10.52.254/24
Group_027	10.10.53.7/24	10.10.54.7/24	DHCP	10.10.53.254/24	10.10.54.254/24
Group_028	10.10.55.7/24	10.10.56.7/24	DHCP	10.10.55.254/24	10.10.56.254/24
Group_029	10.10.57.7/24	10.10.58.7/24	DHCP	10.10.57.254/24	10.10.58.254/24
Group_030	10.10.59.7/24	10.10.60.7/24	DHCP	10.10.59.254/24	10.10.60.254/24
Group_031	10.10.61.7/24	10.10.62.7/24	DHCP	10.10.61.254/24	10.10.62.254/24
Group_032	10.10.63.7/24	10.10.64.7/24	DHCP	10.10.63.254/24	10.10.64.254/24
Group_033	10.10.65.7/24	10.10.66.7/24	DHCP	10.10.65.254/24	10.10.66.254/24
Group_034	10.10.67.7/24	10.10.68.7/24	DHCP	10.10.67.254/24	10.10.68.254/24
Group_035	10.10.69.7/24	10.10.70.7/24	DHCP	10.10.69.254/24	10.10.70.254/24
Group_036	10.10.71.7/24	10.10.72.7/24	DHCP	10.10.71.254/24	10.10.72.254/24
Group_037	10.10.73.7/24	10.10.74.7/24	DHCP	10.10.73.254/24	10.10.74.254/24
Group_038	10.10.75.7/24	10.10.76.7/24	DHCP	10.10.75.254/24	10.10.76.254/24
Group_039	10.10.77.7/24	10.10.78.7/24	DHCP	10.10.77.254/24	10.10.78.254/24
Group_040	10.10.79.7/24	10.10.80.7/24	DHCP	10.10.79.254/24	10.10.80.254/24
Group_041	10.10.81.7/24	10.10.82.7/24	DHCP	10.10.81.254/24	10.10.82.254/24
Group_042	10.10.83.7/24	10.10.84.7/24	DHCP	10.10.83.254/24	10.10.84.254/24
Group_043	10.10.85.7/24	10.10.86.7/24	DHCP	10.10.85.254/24	10.10.86.254/24
Group_044	10.10.87.7/24	10.10.88.7/24	DHCP	10.10.87.254/24	10.10.88.254/24
Group_045	10.10.89.7/24	10.10.90.7/24	DHCP	10.10.89.254/24	10.10.90.254/24
Group_046	10.10.91.7/24	10.10.92.7/24	DHCP	10.10.91.254/24	10.10.92.254/24
Group_047	10.10.93.7/24	10.10.94.7/24	DHCP	10.10.93.254/24	10.10.94.254/24
Group_048	10.10.95.7/24	10.10.96.7/24	DHCP	10.10.95.254/24	10.10.96.254/24
Group_049	10.10.97.7/24	10.10.98.7/24	DHCP	10.10.97.254/24	10.10.98.254/24
Group_050	10.10.99.7/24	10.10.100.7/24 DHCP	    10.10.99.254/24	10.10.100.254/24
Group_051	10.10.101.7/24	10.10.102.7/24 DHCP	    10.10.101.254/24	10.10.102.254/24
Group_052	10.10.103.7/24	10.10.104.7/24 DHCP	    10.10.103.254/24	10.10.104.254/24
Group_053	10.10.105.7/24	10.10.106.7/24 DHCP	    10.10.105.254/24	10.10.106.254/24
Group_054	10.10.107.7/24	10.10.108.7/24 DHCP	    10.10.107.254/24	10.10.108.254/24
Group_055	10.10.109.7/24	10.10.110.7/24 DHCP	    10.10.109.254/24	10.10.110.254/24
Group_056	10.10.111.7/24	10.10.112.7/24 DHCP	    10.10.111.254/24	10.10.112.254/24
Group_057	10.10.113.7/24	10.10.114.7/24 DHCP	10.10.113.254/24	10.10.114.254/24
Group_058	10.10.115.7/24	10.10.116.7/24 DHCP	10.10.115.254/24	10.10.116.254/24
Group_059	10.10.117.7/24	10.10.118.7/24 DHCP	10.10.117.254/24	10.10.118.254/24
Group_060	10.10.119.7/24	10.10.120.7/24 DHCP	10.10.119.254/24	10.10.120.254/24
Group_061	10.10.121.7/24	10.10.122.7/24 DHCP	10.10.121.254/24	10.10.122.254/24
Group_062	10.10.123.7/24	10.10.124.7/24 DHCP	10.10.123.254/24	10.10.124.254/24
Group_063	10.10.125.7/24	10.10.126.7/24 DHCP	10.10.125.254/24	10.10.126.254/24
Group_064	10.10.127.7/24	10.10.128.7/24 DHCP	10.10.127.254/24	10.10.128.254/24
Group_065	10.10.129.7/24	10.10.130.7/24 DHCP	10.10.129.254/24	10.10.130.254/24
Group_066	10.10.131.7/24	10.10.132.7/24 DHCP	10.10.131.254/24	10.10.132.254/24
Group_067	10.10.133.7/24	10.10.134.7/24 DHCP	10.10.133.254/24	10.10.134.254/24
Group_068	10.10.135.7/24	10.10.136.7/24 DHCP	10.10.135.254/24	10.10.136.254/24
Group_069	10.10.137.7/24	10.10.138.7/24 DHCP	10.10.137.254/24	10.10.138.254/24
Group_070	10.10.139.7/24	10.10.140.7/24 DHCP	10.10.139.254/24	10.10.140.254/24
Group_071	10.10.141.7/24	10.10.142.7/24 DHCP	10.10.141.254/24	10.10.142.254/24
Group_072	10.10.143.7/24	10.10.144.7/24 DHCP	10.10.143.254/24	10.10.144.254/24
Group_073	10.10.145.7/24	10.10.146.7/24 DHCP	10.10.145.254/24	10.10.146.254/24
Group_074	10.10.147.7/24	10.10.148.7/24 DHCP	10.10.147.254/24	10.10.148.254/24
Group_075	10.10.149.7/24	10.10.150.7/24 DHCP	10.10.149.254/24	10.10.150.254/24
Group_075	10.10.151.7/24	10.10.152.7/24 DHCP	10.10.151.254/24	10.10.152.254/24
Group_077	10.10.153.7/24	10.10.154.7/24 DHCP	10.10.153.254/24	10.10.154.254/24
Group_078	10.10.155.7/24	10.10.156.7/24 DHCP	10.10.155.254/24	10.10.156.254/24
Group_079	10.10.157.7/24	10.10.158.7/24 DHCP	10.10.157.254/24	10.10.158.254/24
Group_080	10.10.159.7/24	10.10.160.7/24 DHCP	10.10.159.254/24	10.10.160.254/24
Group_081	10.10.161.7/24	10.10.162.7/24 DHCP	10.10.161.254/24	10.10.162.254/24
Group_082	10.10.163.7/24	10.10.164.7/24 DHCP	10.10.163.254/24	10.10.164.254/24
Group_083	10.10.165.7/24	10.10.166.7/24 DHCP	10.10.165.254/24	10.10.166.254/24
Group_084	10.10.167.7/24	10.10.168.7/24 DHCP	10.10.167.254/24	10.10.168.254/24
Group_085	10.10.169.7/24	10.10.170.7/24 DHCP	10.10.169.254/24	10.10.170.254/24
Group_086	10.10.171.7/24	10.10.172.7/24 DHCP	10.10.171.254/24	10.10.172.254/24
Group_087	10.10.173.7/24	10.10.174.7/24 DHCP	10.10.173.254/24	10.10.174.254/24
Group_088	10.10.175.7/24	10.10.176.7/24 DHCP	10.10.175.254/24	10.10.176.254/24
Group_089	10.10.210.7/24	10.10.211.7/24 DHCP	10.10.210.254/24	10.10.211.254/24
Group_090	10.10.181.7/24	10.10.182.7/24 DHCP	10.10.181.254/24	10.10.182.254/24
Group_091	10.10.179.7/24	10.10.180.7/24 DHCP	10.10.179.254/24	10.10.180.254/24
Group_092	10.10.183.7/24	10.10.184.7/24 DHCP	10.10.183.254/24	10.10.184.254/24
Group_093	10.10.185.7/24	10.10.186.7/24 DHCP	10.10.185.254/24	10.10.186.254/24
Group_094	10.10.187.7/24	10.10.188.7/24 DHCP	10.10.187.254/24	10.10.188.254/24
Group_095	10.10.189.7/24	10.10.190.7/24 DHCP	10.10.189.254/24	10.10.190.254/24
Group_096	10.10.191.7/24	10.10.192.7/24 DHCP	10.10.191.254/24	10.10.192.254/24
Group_097	10.10.193.7/24	10.10.194.7/24 DHCP	10.10.193.254/24	10.10.194.254/24
Group_098	10.10.195.7/24	10.10.196.7/24 DHCP	10.10.195.254/24	10.10.196.254/24
Group_099	10.10.197.7/24	10.10.198.7/24 DHCP	10.10.197.254/24	10.10.198.254/24
Group_100	10.10.199.7/24	10.10.200.7/24 DHCP	10.10.199.254/24	10.10.200.254/24
Group_101	10.10.201.7/24	10.10.202.7/24 DHCP	10.10.201.254/24	10.10.202.254/24
Group_102	10.10.203.7/24	10.10.204.7/24 DHCP	10.10.203.254/24	10.10.204.254/24
Group_103	10.10.205.7/24	10.10.206.7/24 DHCP	10.10.205.254/24	10.10.206.254/24
```
