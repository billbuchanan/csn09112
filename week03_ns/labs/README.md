<img src="https://github.com/billbuchanan/csn09112/blob/master/zadditional/top_csn09112.png"/>

# Lab 2: Vyatta and Snort

## Aim
The aim of this lab is to build on the basic Vyatta firewall configuration, adding firewalling, IDS, and other hardening capabilities.

Time to Complete:
4 hours (two supervise hours in the lab, and two additional unsupervised hours).

## Activities:

* Complete Lab 2: Vyatta Firewall and Snort. [<a href="https://github.com/billbuchanan/csn09112/blob/master/week03_ns/labs/lab02_vyatta_ids.pdf" target="_blank">here</a>]. [<a href="https://youtu.be/SJwlt55f_UU" target="_blank">Demo</a>]
* Complete software lab. [here](https://github.com/billbuchanan/csn09112/tree/master/week03_ns/labs/additional_lab).

## Learning activities:
At the end of this lab, you should understand:

* How to use your own credentials to access the vSoC Cloud.
* How to remotely configure a Vyatta firewall for zones, and set up the firewalling.
* Set-up Snort IDS system on a host and create useful rules to detect potential attacks.

## Reflective statements (end-of-exercise):
What is the most important things when setting up a host, in order that it can connect with other networks?


Reflect on which types of attacks the firewall rules can mitigate, and which the IDS system can help highlight:



# A	Setting up the network
Figure 1 outlines the setup of the lab for routing, where we will assign three network addresses. Again, Interfaces which are connected to the Vyatta firewall will be able to route, but we have to use NAT to allow the DMZ and private networks to connect to the public network.

Our first task is to route through the Vyatta firewall to connect two networks. In the lab you will be assigned two networks in the form:

10.10.x.0/24	10.10.y.0/24

Demo: [here](https://youtu.be/SJwlt55f_UU)

![Lab](https://github.com/billbuchanan/csn09112/blob/master/zadditional/overview.png)
Figure 1: Lab setup (eth0 – Public, eth1 – Private, eth2 – DMZ)  with 10.10.z.z

![Lab](https://github.com/billbuchanan/csn09112/blob/master/zadditional/overview_172.png)
Figure 1: Lab setup (eth0 – Public, eth1 – Private, eth2 – DMZ) with 172.16.z.z

Log into vSphere and locate the CSN09412 folder. Locate your matriculation number and you will be allocated two network addresses (for Private and DMZ). Draw your own network diagram here, by filling-in the blank boxes, with the allocated networks, subnets, and IP addresses:

![Lab](https://github.com/billbuchanan/csn09112/blob/master/zadditional/overview02.png)
Figure 2: Your network setup (Note: Gateway address is 10.221.3.254)

# B	Configure Router/Firewall for Remote Administration
First reset your firewall by either reverting back to the original instance or using the command:
```
load /opt/vyatta/etc/config.boot.default
```
We typically don’t use the console terminal of a firewall for configuration. In the following we will enable one port on the firewall, and then configure it through a remote connection. First configure your Vyatta firewall networking with the following:

```
$ configure
# set interfaces ethernet eth2 address 10.10.y.254/24
# set protocols static route 0.0.0.0/0 next-hop 10.221.3.254
```

and then start the SSH server on the Vyatta firewall:

```
# set service ssh
```

Check the configuration using:

```
# show 
# show interfaces
# show service
```

If everything is correct commit the changes, and review the configuration:

```
# commit
# show config
```

 

Now setup your Kali host on the DMZ for networking, and so it will be able to connect to the Vyatta firewall using remote admin with the Telnet service:

```
sudo ip link set eth0 up
sudo ip addr add 10.10.y.8/24 dev eth0
sudo ip route add default via 10.10.y.254 dev eth0
```

Now from Kali, check the connectivity using ping to your local connection and the gateway:

Can you ping them: [Yes] [No]

# C	Configuring the firewall from Kali (DMZ)
Now we will configure the firewall by creating a file, and copying-and-pasting the config from the file to the firewall via a remote admin session with SSH.

First create an empty file named ``vpart01.txt`` and paste the following config from: 

https://asecuritysite.com/vpart01.txt

or use:
```
wget https://asecuritysite.com/vpart01.txt
```


Note you need to use the VMRC console for copy-and-paste to work. Now edit the ‘x’ (Private) and ‘y’ (DMZ) values for your network:

```
set interfaces ethernet eth0 address dhcp
set interfaces ethernet eth1 address 10.10.x.254/24 
set interfaces ethernet eth2 address 10.10.y.254/24 
set protocols static route 0.0.0.0/0 next-hop 10.221.3.254

set nat source rule 1 outbound-interface eth0
set nat source rule 1 source address 10.10.x.0/24 
set nat source rule 1 translation address masquerade

set nat source rule 2 outbound-interface eth0
set nat source rule 2 source address 10.10.y.0/24 
set nat source rule 2 translation address masquerade 
```

Now, from Kali, create an SSH connection to the default gateway on the firewall (172.16.x.254):

```
ssh 10.10.x.254 -l vyos
```

 
Now log into the firewall, and go into configuration mode and copy-and-paste the config  from your config file, check the config, and then commit the changes if they are correct:

```
Login:
Password: ******
$ configure
# <paste-config>
# commit
```

Now setup your Ubuntu host with 10.10.x.7 with a default gateway of 10.10.x.254, and the Windows 7 host with 10.10.y.7 with a default gateway of 10.10.y.254. Note, on Kali and Ubuntu, you need to edit /etc/resolv.conf and add a nameserver of 10.221.3.254.

From Kali, can you ping the local host, the Ubuntu host, the Windows host, the firewall ports, 8.8.8.8 and google.com? [Yes][No]

From Windows, can you ping the local host, the Ubuntu host, the Kali host, the Windows host, the firewall ports, 8.8.8.8 and google.com? [Yes][No]

From Ubuntu, Kali and Windows, can you access google.com from a browser [Yes][No]

Is everything working on your network? [Yes][No]


Now nmap from the Ubuntu host to the Windows host. Which ports are accessible:

[ftp, ssh, http, https] 


Now nmap from the Windows host to the Ubuntu host. Which ports are accessible:

[ftp, ssh, http, https, rpcbind, vnc]



# D	Setting up Firewall Rules
Now we will setup firewall rules between zones (networks) connected to the firewall. In this case we will enable all the connections from the private network to the DMZ, but only allow TCP ports 80 and 443 to go through from the DMZ to the private network. All other connections will be disallowed. If we allow the connections from the private and the DMZ, we must remember the connection to allow it back from the DMZ to the private network, thus we define that we accepted established connections.
Now we will configure the next part of the firewall by copying-and-pasting the config to the firewall. First download the following config:


https://asecuritysite.com/vpart02.txt

```
set zone-policy zone private  description  "Inside" 
set zone-policy zone public  description  "Outside" 
set zone-policy  zone  dmz description "DMZ"

set zone-policy zone public  interface  eth0 
set zone-policy zone private interface  eth1 
set zone-policy  zone  dmz  interface eth2

set firewall	name	dmz2private description	"DMZ to private" 
set firewall	name	dmz2private rule	1	action	accept
set firewall	name	dmz2private rule	1	state	established	enable 
set firewall	name	dmz2private rule	1	state	related enable
set firewall name  dmz2private rule  10  action accept
set firewall	name	dmz2private rule	10	destination	port	80,443 
set firewall	name	dmz2private rule	10	protocol tcp

set	firewall	name	private2dmz	description	"private to DMZ"
set	firewall	name	private2dmz	rule	1	action	accept
set	zone-policy	zone	private from	dmz firewall	name	dmz2private
set	zone-policy	zone	dmz from	private firewall	name	private2dmz
```

and paste it into your firewall, check the config, and then commit.

From Ubuntu, can you ping the local network, the Windows host, the firewall ports and 8.8.8.8.  Can you now ping?

[Yes/No] 

From Ubuntu, can you access the Web server on Windows from a browser [Yes/No] 

From Windows, can you ping the local network, the Windows host, the firewall ports and 8.8.8.8. Can you now ping?

[Yes/No] 

From Windows, can you access the Web server on Ubuntu from a browser [Yes/No]

From Ubuntu and Windows, can you access Google.com from a browser [Yes/No] 

Now nmap from the Ubuntu host to the Windows host. Which ports are accessible:

[http, https]

Now nmap from the Windows host to the Ubuntu host. Which ports are accessible:

[]

Explain the operation of the network with the new network settings:




# E	Allowing access to the public network
You should not currently be able to connect from the private network to the public one. Now setup this connection:

http://asecuritysite.com/vpart03.txt

```
set firewall	name	private2public description	"private to public" 
set firewall	name	private2public rule	1	action	accept
set zone-policy	zone	public from	private firewall	name	private2public

set firewall	name	public2private description	"public to private" 
set firewall	name	public2private rule	1	action	accept
set firewall	name	public2private rule	1	state	established	enable 
set firewall	name	public2private rule	1	state	related enable
set zone-policy	zone	private from public firewall	name	public2private

commit
```

You should now be able to connect from the private network to the public one. 

From Ubuntu, can you access 8.8.8.8 with ping? [Yes/No]
From Ubuntu, can you access google.com with ping? [Yes/No]
From Ubuntu, can you access google.com from a browser? [Yes/No]

From Windows, can you access 8.8.8.8 with ping? [Yes/No]
From Windows, can you access google.com with ping? [Yes/No]
From Windows, can you access google.com from a browser? [Yes/No]


Now create your own config and allow the DMZ to communicate with the public network.

You should now be able to connect from the private network to the public one. 

From Ubuntu, can you access 8.8.8.8 with ping? [Yes/No]
From Ubuntu, can you access google.com with ping? [Yes/No]
From Ubuntu, can you access google.com from a browser? [Yes/No]

From Windows, can you access 8.8.8.8 with ping? [Yes/No]
From Windows, can you access google.com with ping? [Yes/No]
From Windows, can you access google.com from a browser? [Yes/No]

Which configuration commands have you used:




Can you connect your Windows host to the Google.com? [Yes][No]
Can you connect your Ubuntu host to the Google.com? [Yes][No]




# F	Snort IDS
Snort is one of the most popular intrusion detection systems, where an agent is used to detect network threats. On the Windows and Ubuntu systems, create simple Snort rules files both called mysnort.rules, and add the following rules:

```
alert tcp any any -> any any (sid:999;content:"napier"; nocase; msg:"Napier detected") 
alert tcp any any -> any any (sid:1000;content:"fred"; nocase; msg:"Fred detected")
```

The format of Snort Detection Rules are as follows:

```
action protocol src-ip src-port > dest-ip dest-port (packet-payload-params output-msg) 
[pass|log|alert] [ip|icmp|tcp|udp] [any|IP] [any|port] > [any|IP] [any|port] ([content:“searchstring”;], [nocase;], [msg:”alert message”;] sid:ruleid;)
```

This should detect outgoing traffic which has the word “napier” or “fred” in the payload. From the Windows system check the Snort options:

```
snort -?
```

Next run Snort using the required network interface: (Use the –W flag to check your available interfaces)

```
snort -c mysnort.rules -i 1 -p -l log -K ascii
```

From the Linux system run Snort (used ifconfig to see your interfaces):

```
snort -c mysnort.rules -i eth11 -p -l log -K ascii
```

Snort should now be running using the rules file to match against packets on the specified network interface, and write alerts and log information on any matches to the log folder.

# G	Software Tutorial
Complete the software tutorial at: 

http://asecuritysite.com/csn09412/software01

# Appendix
```
configure

set interfaces ethernet eth0 address dhcp
set interfaces ethernet eth1 address 172.16.x.254/24 
set interfaces ethernet eth2 address 172.16.y.254/24 
set system gateway 10.221.3.254

set nat source rule 1 outbound-interface eth0
set nat source rule 1 source address 172.16.x.0/24 
set nat source rule 1 translation address masquerade

set nat source rule 2 outbound-interface eth0
set nat source rule 2 source address 172.16.y.0/24 
set nat source rule 2 translation address masquerade

set zone-policy zone private  description  "Inside" set zone-policy zone public  description  "Outside" set zone-policy  zone  dmz description "DMZ"

set zone-policy zone public  interface  eth0 
set zone-policy zone private interface  eth1 
set zone-policy  zone  dmz  interface eth2

set firewall	name	dmz2private description	"DMZ to private" 
set firewall	name	dmz2private rule	1	action	accept
set firewall	name	dmz2private rule	1	state	established	enable 
set firewall	name	dmz2private rule	1	state	related enable
set firewall  	name  dmz2private rule  10  	action accept
set firewall	name	dmz2private rule	10	destination	port	80,443 
set firewall	name	dmz2private rule	10	protocol tcp

set firewall	name	private2dmz description	"private to DMZ" 
set firewall	name	private2dmz rule	1	action	accept

set zone-policy	zone	private from	dmz firewall	name	dmz2private
set zone-policy	zone	dmz from	private firewall	name	private2dmz


set firewall	name	private2public description	"private to public" 
set firewall	name	private2public rule	1	action	accept
set zone-policy  	zone  public from  private firewall  name private2public

set firewall	name	public2private description	"public to private" 
set firewall	name	public2private rule	1	action	accept
set firewall	name	public2private rule	1	state	established	enable set firewall	name	public2private rule	1	state	related enable
set zone-policy  	zone  private from  public firewall  name public2private
```

http://asecuritysite.com/vfinal.txt







## Lab setup
<img src="https://github.com/billbuchanan/csn09112/blob/master/zadditional/overview.png"/>

## Quick guide
For Ubtuntu configuration:
```
ip addr add 172.16.10.7 dev eth1
route add default gw 172.16.10.254 eth11
```
Edit /etc/resolv.conf:
```
nameserver 8.8.8.8
nameserver 10.221.3.254
```





