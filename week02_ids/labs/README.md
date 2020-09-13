<img src="https://github.com/billbuchanan/csn09112/blob/master/zadditional/top_csn09112.png"/>

# Lab 1: Vyatta Firewalls

## Aim
The  aim  of  this  lab  is  to  introduce  the  vSoC  virtualisation  teaching  platform  and  VSphere client  access  to  your  own  virtual  machines  and  to  understand  how  to  configure  a  Vyatta firewall  for  NAT  and  firewall  rules, demonstrating  some  fundamentals  around  network security and device configuration. It is accessed from:

```
vsoc.napier.ac.uk
```


## Time to Complete
4 hours (two supervise hours in the lab,and two additional unsupervised hours).

## Activities

Vyatta Firewall lab. [Here](https://github.com/billbuchanan/csn09112/blob/master/week02_ids/labs/lab01_Vyatta.pdf")

Video: [Here](https://www.youtube.com/watch?v=ACldSA_uKM0) 

## Learning activities
At the end of this lab, you should understand:

* How to access the vSoC Cloud, working with your ownfolder within CSN09412.</li>
* How to launch virtual machines, such as your Ubuntu, Windows Server, and Vyatta ones.</li>
* How to configure the network settings of the Ubuntu and Windows Server machines, as well as using some basic Linux and Windows commands.</li>
* How  to  configure  the  Vyatta  firewall,  for  basic  routing,  NAT,  and  filtering -to  grant  or block access to certain types of packets and protocols.</li>
* How to use Wireshark to capture network packets for deep analysis, highlighting certain details such as the difference between the Telnet and SSH services</li>




## Reflective statements (end-of-exercise):
•	What is the most important things when setting up a host, in order that it can connect with other networks?
•	With the Vyatta firewall, how does the firewall protect against threats?



## A	Setting up the network
Figure 1 outlines the setup of the lab for routing, where we will assign three network addresses. Interfaces which are connected to the Vyatta firewall will be able to route, but we have to use NAT to allow the DMZ and private networks to connect to the public network. 

Our first task is to route through the Vyatta firewall to connect two networks. In the lab you will be assigned two networks in the form: 

10.10.x.0/24		10.10.y.0/24   

Part 1 Demo:  [here](https://youtu.be/ACldSA_uKM0)
 
![Lab](https://github.com/billbuchanan/csn09112/blob/master/zadditional/overview.png)
Figure 1: Lab setup (eth0 – Public, eth1 – Private, eth2 – DMZ)


Log into vSphere (vsoc.napier.ac.uk) and locate the CSN09112 folder. Locate your matriculation number and you will be allocated a group number:

Group Number: 


Note: Sometimes the network names are different, such as Eth3, Eth4 and Eth5. Assume that the first network name is Public, the second is the Private network, and the third is the DMZ.

Use the network diagram in Figure 2, filling in the boxes with your addressing, the allocated networks, subnets, and IP addresses, and use as reference, as you complete the lab.

* Vyatta. 		User: vyatta, Password: vyatta
* Windows 2003: 	User: Administrator, Password: napier
* Ubuntu:		User: root, password: napier123
* Kali:			User: root, password: toor

 
![Lab](https://github.com/billbuchanan/csn09112/blob/master/zadditional/overview02.png)
Figure 2: Your network setup

Select your Ubuntu host (User: napier, Password: napier123) and configure for 10.10.x.7 with a default gateway of 10.10.x.254 and a subnet mask of 255.255.255.0.

Can you ping the 10.10.x.7 port from the host selected? Yes/No

Select your Windows server (User: Administrator, Password: napier) and configure it at 10.10.y.7 with a default gateway of 10.10.y.254 and a subnet mask of 255.255.255.0.

Can you ping the 10.10.y.7 port from the host selected? Yes/No

From each of your hosts, can you ping the other host? Yes/No

Why can’t you ping the other host?


Note. For Linux uses the commands:

```
sudo ifconfig eth11 10.10.x.7 netmask 255.255.255.0 up
sudo route add default gw 10.10.x.254
```

## Routing between connected networks
Start up your Vyatta firewall. 
Login to the firewall, with: (User: vyatta, Password: vyatta)

View the current configuration with the command:

```
show configuration
```

Initially erase the configuration in the firewall, and reboot it, with:

```
cp /opt/vyatta/etc/config.boot.default /opt/vyatta/etc/config/config.boot

reboot
```

Next perform the following:

Setup a few simple things, such as the hostname, a username and password, and so on:

```
$ configure
# set system host-name yourname
# set system login user yourname authentication plaintext-password yourpass
```

Configure the firewall using the following commands (changing the x and y for your net):

```
$ configure
# set interfaces ethernet eth0 address dhcp
# set interfaces ethernet eth1 address 10.10.x.254/24
# set interfaces ethernet eth2 address 10.10.y.254/24
# set system gateway 10.221.3.254
```

Before you commit the configuration, can you ping the 10.10.y.7 port from the host on at 10.10.x.7? Yes/No

Now go ahead and commit the configuration with:
```
# commit
```

And exit the current configuration mode with:

```
# exit
```

Can you ping the 10.10.y.7 port from the host on 10.10.x.7? Yes/No

Can you ping the 10.10.x.7 port from the host on 10.10.y.7? Yes/No

Now run Wireshark on your hosts, and repeat. Examine you network trace, and determine the successful ping request, and ping reply. Which ICMP type codes are used for the request and the successful reply:



What do the following commands do:

show configuration:

show interface:



Now delete the IP address on the eth1 interface on the firewall, and reassess:

Can you ping the 10.10.y.7 port from the host on the 10.10.x.7? Yes/No

Can you ping the 10.10.x.7 port from the host on the 10.10.y.7? Yes/No

Now run Wireshark on your hosts, and repeat. Examine you network trace, and determine the unsuccessful ping request, and ping reply. Which ICMP type codes are used for the request and the unsuccessful reply:

Note:

```
$ configure
# delete interfaces ethernet eth1 address 10.10.x.254/24
# commit
```

Now, reapply the IP address, and using the arp –a command, determine the MAC addresses of the gateway adapter, and check this against the configuration of the firewall.

What are the MAC addresses of the firewall:


Now with a browser on each host, access the Web server on the other network.

Can you access the Web server on the 10.10.y.7 from 10.10.x.7? Yes/No

Can you access the Web server on the 10.10.x.7 from 10.10.y.7? Yes/No


As before, disable the IP address on the eth1 port, and reapply (make sure you refresh the cache on the browser):

Can you access the Web server on the 10.10.y.7 from 10.10.x.7? Yes/No

Can you access the Web server on the 10.10.x.7 from 10.10.y.7? Yes/No


Reapply everything as before, and test that it still works.

Startup Wireshark on each of your hosts, and capture traffic.

Run an nmap scan from the Windows host to the Linux one. What ports are open on the Linux host:

Run an nmap scan from the Linux host to the Windows one. What ports are open on the Windows host:


Commands:
```
nmap –sS 10.1.1.0/24
```

## Setting up NAT
Now we need to setup NAT to map the addresses on the DMZ and the private network to an address taken from the public network. We are using NAT overloading (or NAT masquerade) which will map the private addresses to a public address (taken from eth0).

To map the addresses from the private to the public network:

```
# set nat source rule 1 outbound-interface eth0
# set nat source rule 1 source address 10.10.x.0/24
# set nat source rule 1 translation address masquerade
# commit
# save
```

To map the addresses from the DMZ to the public network:

```
# set nat source rule 2 outbound-interface eth0
# set nat source rule 2 source address 10.10.y.0/24
# set nat source rule 2 translation address masquerade
# commit
# save
```

You should now have a network connection from the private and DMZ networks to the public network. On your Ubuntu host change name server to 10.221.3.254 with:

```
sudo nano /etc/resolv.conf
```

And change the nameserver to:

```
nameserver 10.246.3.254
```

Now can you ping 10.221.3.254 from Ubuntu? Yes/No
Now can you ping 10.221.3.254 from Windows 2003? Yes/No

Now can you ping 8.8.8.8 from Ubuntu? Yes/No
Now can you ping 8.8.8.8 from Windows 2003? Yes/No

Now can you access Google.com from Ubuntu? Yes/No
Now can you access Google.com from Windows 2003? Yes/No

## Setting up services on firewall
Now save your configuration in edit mode with:

```
# save
# exit
$ reboot
```

You can now reboot the firewall (use the command reboot), and login with your new username and password.

Now restart Wireshark on the Linux install. Next enable the Telnet server on the Vyatta firewall with:

```
# set service telnet
# commit
```

Now telnet into the Vyatta firewall.

Was the login successful? Yes/No

Using the TCP Stream trace on the Wireshark trace. What can you observe from the stream? Can you see the password for the login?


Note: sudo wireshark

Now restart Wireshark on the Linux install. Next enable the SSH server on the Vyatta firewall with:

```
# set service ssh
# commit
```

Now ssh into the Vyatta firewall from the Linux host using:

```
ssh 10.10.y.254 –l username 
```

Was the login successful? Yes/No

Using the TCP Stream trace on the Wireshark trace. What can you observe from the stream? Can you see the password for the login?



Check to see if you have a Kali instance in your group folder. If so, complete the following:

From your Kali instance, can you ping each of the interfaces on the firewall:  Yes/No

From your Kali instance, can you ping each of the interfaces on the hosts:  Yes/No

Now setup the default gateway of your Kali host to be the IP address of your eth0 port on your firewall. Are you now able to ping your Ubuntu and Windows machines?

If so, why can you now ping them?


## Firewalling
The Vyatta firewall uses zones to define security regions. In this case we can setup public, dmz and private. Then we apply firewall rules to define how the traffic between the zones is filtered. In this case we will only setup the traffic between the dmz and private, with two rules: dmz2private and private2dmz. Possible filtering is to allow connections on certain ports from private to dmz, but block all connections that are initiated in the dmz for the private region. Figure 3 outlines the setup.

 
Figure 3: Zone and firewall rule setup

To enable firewalling we first define some zones (private, public, and dmz):

```
set  zone-policy  zone  private  description  "Inside”
set  zone-¬policy  zone  public  description  "Outside”
set  zone-¬policy  zone  dmz description  "DMZ"
```

These zones are then applied onto the interfaces:

```
set  zone-¬policy  zone  public  interface  eth0
set  zone-¬policy  zone  private interface  eth1
set  zone-¬policy  zone  dmz  interface  eth2
```

Now try to access services from the Windows instance to the Linux one:

Can you access any of these services:

* Web Yes/No
* Telnet Yes/No
* FTP Yes/No
* SMTP Yes/No

Now we will allow only established connections from the DMZ to the private network:

```
set  firewall  name  dmz2private description  "DMZ to private"
set  firewall  name  dmz2private rule  1  action  accept
set  firewall  name  dmz2private rule  1  state  established  enable
set  firewall  name  dmz2private rule  1  state  related enable
```

Then we will accept connections on port 80 and 443 from the private network to the DMZ:

```
set  firewall  name  private2dmz description  "private to DMZ"
set  firewall  name  private2dmz rule  1  action  accept
set  firewall  name  private2dmz rule  1  state  established  enable
set  firewall  name  private2dmz rule  1  state  related enable
set  firewall  name  private2dmz rule  10  action  accept
set  firewall  name  private2dmz rule  10  destination  port  80,443  
set  firewall  name  private2dmz rule  10  protocol tcp
```

Now we have zones of public, dmz and private, and rules of dmz2private and private2dmz. To apply the rules to zones we complete with:

```
set  zone-¬policy  zone  private from  dmz firewall  name  dmz2private
set  zone-¬policy  zone  dmz from  private firewall  name  private2dmz
```

Commit this, and try and connect from each of the networks to the other:

From the Linux machine on the private network access the following services on the Windows server in the DMZ:

* Web Yes/No
* Telnet Yes/No
* FTP Yes/No
* SMTP Yes/No

From the Windows machine on the public network access the following services on the Linux server in the private network:

* Web Yes/No
* Telnet Yes/No
* FTP Yes/No
* SMTP Yes/No

Are the results as expected?

Now enable Telnet, FTP and SMTP from the private network to the DMZ.

Enable Wireshark on the Windows host, and observe the trace when you nmap from the Linux host. What can you observe:



Enable Wireshark on the Linux host, and observe the trace when you nmap from the Windows host. What can you observe:


Note. You can test whether the port is open by using telnet on the given port number:

Test FTP: telnet 10.10.x.7 21

Test Telnet: telnet 10.10.x.7 23

Test HTTP: telnet 10.10.x.7 80

Test SMTP: telnet 10.10.x.7 25

If you receive a response, the port is open, if not it is closed.


Check to see if you have a Kali instance in your group folder. If so, complete the following:

From your Kali instance, Can you ping each of the interfaces on the firewall:  Yes/No

From your Kali instance, Can you ping each of the interfaces on the hosts:  Yes/No

## DoS Protection
A particularly difficult area to protect against is Denial of Service (DoS). The Vyatta firewall has protection for this, where it limits the number of connections over a given amount of time. Now let’s limit the number of Web connections to 5 in 10 seconds:

```
set  firewall  name  private2dmz rule 5 action  drop
set  firewall  name  private2dmz rule 5 protocol tcp
set  firewall  name  private2dmz rule 5 destination  port 21,23,25,80,443
set  firewall  name  private2dmz rule 5 recent  count  5  
set  firewall  name  private2dmz rule 5 recent time 10
```

Commit this.

Run Wireshark on the Windows host. From the Linux host on the private network, now try and hping from the Linux host to the Windows host. What do you observe from the Wireshark trace and also from the return from hping:


How many connections where accepted before it stopped?

Note. To perform an hping on 10.1.1.7 on port 80:

```
hping 10.1.1.7 -S -V -p 80
```
## Appendix
Now restart Wireshark on the Linux install. Next enable the DHCP server for the Linux host on the Vyatta firewall with:

# set service dhcp-server shared-network-name ETH1 subnet 10.10.x.0/24 start 10.10.x.9 stop 10.10.x.100
# set service dhcp-server shared-network-name ETH1 subnet 10.10.x.0/24 default-router 10.10.x.254
# commit

Now renew the IP address on the Linux host with:

sudo dhclient –r
sudo dhclient 

What is the IP address that was allocated to the Linux instance from the DHCP server:

What is the data packet that is sent to release the IP address from the interface:

IP addresses used: 
UDP ports used:
Bootstrap Message:

What is the handshake that is used to gain the IP address from the DHCP server:


 
 

# IP Allocation

<p>IP Allocation</p>
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

Allocated	Ubuntu	        Windows	        Em0	    Em1 (Private)	Em2 (DMZ)
-----------------------------------------------------------------------------------
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

Allocated	Ubuntu	        Windows	        Em0	    Em1 (Private)	Em2 (DMZ)
-----------------------------------------------------------------------------------
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

Allocated	Ubuntu	        Windows	        Em0	    Em1 (Private)	Em2 (DMZ)
-----------------------------------------------------------------------------------
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

Allocated	Ubuntu	        Windows	        Em0	    Em1 (Private)	Em2 (DMZ)
-----------------------------------------------------------------------------------
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

Allocated	Ubuntu	        Windows	        Em0	    Em1 (Private)	Em2 (DMZ)
-----------------------------------------------------------------------------------
Group_101	10.10.201.7/24	10.10.202.7/24 DHCP	10.10.201.254/24	10.10.202.254/24
Group_102	10.10.203.7/24	10.10.204.7/24 DHCP	10.10.203.254/24	10.10.204.254/24
Group_103	10.10.205.7/24	10.10.206.7/24 DHCP	10.10.205.254/24	10.10.206.254/24
```


## Quick guide
For Ubtuntu configuration:

```
ip addr add 192.1.1.1 dev eth1
route add default gw 192.168.1.254 eth0
nano /etc/resolve.conf 
```

Within resolve.conf add the line:

```
name-server 10.221.3.354
```

For vyatta:
```
$ configure
# set system host-name yourname
# set system login user yourname authentication plaintext-password yourpass
# set interfaces ethernet eth0 address dhcp
# set interfaces ethernet eth1 address 10.10.x.254/24
# set interfaces ethernet eth2 address 10.10.y.254/24
# set system gateway 10.221.3.254
```






