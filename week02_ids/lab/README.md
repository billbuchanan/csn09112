<img src="https://github.com/billbuchanan/csn09112/blob/master/zadditional/top_csn09112.png"/>

# Lab 1: Virtualised Infrastructures

## Aim
The aim of this lab is to build a network of hosts and get the firewall to allow intercommunication between a range of hosts.

## Activities

Complete Lab 3: The lab is [here](https://github.com/billbuchanan/csn09112/blob/master/week04_ciphers/labs/csn09112_lab03.pdf) and there a demo of the lab [here](https://www.youtube.com/watch?v=qIA3LnKTI6k).</p>



## Lab setup
Our challenge is to setup MyBank Incorp, where each of you will be allocated a network and hosts to configure and get on-line (Figure 1). You have a pfSense firewall, a Ubuntu (Private) host, a Windows (DMZ) host, a Metasploitable (DMZ) host and a Kali (DMZ) host to achieve your objectives. 


![Lab](https://github.com/billbuchanan/csn09112/blob/master/week04_ciphers/labs/pfsense1.png)  
Figure 1: Lab setup (le0 – Public, le1 – Private, le2 – DMZ)  with 10.10.z.z

## Quick guide</h2>
For Ubtuntu configuration, for 10.10.x.7:

```
sudo ip link set ens160 up
sudo ip addr add 10.10.x.7/24 dev ens32
sudo ip route add default via 10.10.x.254 dev ens32
nano /etc/resolv.conf and change "nameserver 146.176.1.5"
```



## Setting up the network
In this lab we will connect multiple firewalls to the main gateway, and be able to complete the challenges in Table 1. You will be given two things:

Group Number:

Your networks will be: 10.10.x.0/24  10.10.y.0/24  

Demo: [here](https://youtu.be/g7dzDM4aU0k)


## B Initial Firewall Creation
Now go to your folder, and select the firewall for your network. Next configure the Ubuntu server in the Private zone, and the Windows server in the DMZ.

| Perform the following: |
|-------------------------------|
| Boot your firewall, and say no to setting up VLANs.
| Now setup the first three networks adapters with le0 (WAN), le1 (LAN) and le2 (OPT1).
| Check that you have been granted an IP address on the WAN (le0) port. What address is it:
| Can you ping the main gateway from the firewall (10.221.3.254) and your own WAN port?  Yes/No

Now, we want to set up your private network gateway.

| Perform the following: |
|-------------------------------|
| Select the (2) option to change the IP addresses on the interfaces. Setup the IP address for the le1 interface to 10.10.x.254/24. 
| Note the URL that you can configure your firewall. What is the URL:

You are all finished in doing the initial configuration on the firewall. We will now go ahead and configure the hosts and gain access to the firewall from a Web browser.

## C Host setup
Now we will configure the hosts to sit on the Private and DMZ networks.

Setup the Ubuntu host to connect to 10.10.x.7/24 with a default gateway of your firewall port (10.10.x.254/24).

```
sudo ip link set ens32 up
sudo ip addr add 10.10.x.7/24 dev ens32
sudo ip route add default via 10.10.x.254 dev ens32
```

### Ubuntu host setup
Next setup the nameserver on the Ubuntu host by editing the /etc/resolv.config and adding a nameserver:
```
sudo nano /etc/resolv.conf
```
then add:
```
nameserver 10.221.3.254
```

### Kali host setup
Do the same for your host on the Kali host on the DMZ. Setup the Kali host to connect to 10.10.y.8/24 with a default gateway of your firewall port (10.10.y.254/24).

```
sudo ip link set eth0 up
sudo ip addr add 10.10.y.8/24 dev eth0
sudo ip route add default via 10.10.y.254 dev eth0
```

Next setup the nameserver on the Kali host by editing the /etc/resolv.config and adding a nameserver:
```
sudo nano /etc/resolv.conf
```
then add:
```
nameserver 10.221.3.254
```
### Metasploitable host setup
Next setup your Metasploitable host on the DMZ (User: msfadmin, Password: napier123). Setup the Metasploitable host to connect to 10.10.y.9/24 with a default gateway of your firewall port (10.10.y.254/24).
```
sudo ip addr add 10.10.y.9/24 dev eth0
sudo ip route add default via 10.10.y.254 dev eth0
```

### Windows host setup
On the Windows server modify the static address on the interface with:

```
IP: 10.10.y.7
Subnet mask: 255.255.255.0
Gateway: 10.10.y.254
DNS: 10.221.3.254
```

### Firewall  setup
Now, we will finalise the configuration of the firewall. Log into the firewall from the Ubuntu host on the Private zone with:

```
http://10.10.x.254
```

Username: admin, Password: pfsense

Setup the required IP on the DMZ (10.10.y.254) and subnet mask.

On the firewall, from Diagnostics, view the ARP cache. Which addresses are in the cache?


On the firewall, from Diagnostics, ping each of the 10.10.x.254 and 10.10.x.7 interfaces from the LAN network. Can you ping them? [Yes/No]

 
On the Windows host, ping 10.10.y.254 and 10.10.y.7 interfaces. Can you ping them? [Yes/No] Why can’t you ping the 10.10.y.254 interface?



On the firewall, create a rule which allows a host on the DMZ to use ICMP to any destination.

On the Windows host, ping 10.10.y.254 and 10.10.y.7 interfaces. You should now be able to ping them.

On the Windows host, ping 10.10.x.254 and 10.10.x.7 interfaces. You should now be able to ping them.

On the firewall, create a rule which allows the Public network to ping both the DMZ and Private network. From the firewall, can you ping the hosts in the DMZ and Private network from the WAN port?

Now from the Windows host and the Ubuntu host, ping all the key addresses, including the gateway 10.221.3.254 and 10.200.0.2.




# Software Tutorial
Complete the software tutorial at: 

http://asecuritysite.com/csn09112/software02


# Appendix
User logins: 

Ubuntu:- User: napier, Password: napier123  
Kali:-  User: root, Password: toor  
Windows:-		User: Administrator, Password: napier123  
pfsense:- User: admin, Password: pfsense  
Metasploitable:- User: msfadmin, Password: napier123  


