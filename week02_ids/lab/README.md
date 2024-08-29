<img src="https://github.com/billbuchanan/csn09112/blob/master/zadditional/top_csn09112.png"/>

# Lab 1: Virtualised Infrastructures

## Aim
The aim of this lab is to build a network of hosts and get the firewall to allow intercommunication between a range of hosts.

## Activities

Complete Lab 1: The lab is [here](https://github.com/billbuchanan/csn09112/blob/master/week04_ciphers/labs/csn09112_lab03.pdf) and there a demo of the lab [here](https://www.youtube.com/watch?v=qIA3LnKTI6k).</p>



## Lab setup
Our challenge is to set up MyBank Incorp, where each of you will be allocated a network and hosts to configure and get online (Figure 1). You have a pfSense firewall, a Ubuntu (Private) host, a Windows (DMZ) host, a Metasploitable (DMZ) host, a Kali (DMZ) host and a Kali (Public) host to achieve your objectives. 


![Lab](https://github.com/billbuchanan/csn09112/blob/master/week04_ciphers/labs/pfsense1.png)  
Figure 1: Lab setup (le0 – Public, le1 – Private, le2 – DMZ)  with 10.10.z.z

## Quick guide</h2>
For Ubuntu configuration, for 10.10.x.7:

```
sudo ip link set ens160 up
sudo ip addr add 10.10.x.7/24 dev ens160
sudo ip route add default via 10.10.x.254 dev ens32
nano /etc/resolv.conf and change "nameserver 146.176.1.5"
```



## Setting up the network
In this lab, we will connect our firewall to the main gateway and be able to complete the challenges in Table 1. You will be given two things:

Group Number:

Your networks will be: 10.10.x.0/24  10.10.y.0/24  

Demo: [here](https://www.youtube.com/watch?v=qIA3LnKTI6k))


## B Initial Firewall Creation
Power up your Pfsense firewall. **Do not set VLANs**, and enable the interfaces of:

* vmx0. WAN.
* vmx1. Private.
* vmx2. DMZ

Let the firewall boot up, and then select **(2) Setup IP Interface(s)**, and set the LAN interface to have an IP address of 10.10.x.254/24. 

Now we will configure the hosts to sit on the Private and DMZ networks.

## C Ubuntu setup
Set up the Ubuntu host to connect to 10.10.x.7/24 with a default gateway of your firewall port (10.10.x.254/24).

```
sudo ip link set ens160 up
sudo ip addr add 10.10.x.7/24 dev ens160
sudo ip route add default via 10.10.x.254 dev ens160
```
Can you ping the default gateway?

Next setup the nameserver on the Ubuntu host by editing the /etc/resolv.config and adding a nameserver:

```
sudo nano /etc/resolv.conf
```
then add:
```
nameserver 146.176.1.5
```

### Kali host setup
Do the same for your host on the Kali host on the DMZ. Set up the Kali host to connect to 10.10.y.8/24 with a default gateway of your firewall port (10.10.y.254/24).

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

### Windows 7 host setup
On the Windows server, modify the static address on the interface with:

```
IP: 10.10.y.7
Subnet mask: 255.255.255.0
Gateway: 10.10.y.254
DNS: 146.176.1.5
```


### Kali (Public) host setup
On the Kali public host, verify that it can ping the default gateway (10.221.3.254), 8.8.8.8 and also google.com? 

| | |
|-|-|
| Can you ping 10.221.3.254? | [Yes/No] |
| Can you ping 8.8.8.8? | [Yes/No] | 
| Can you ping Google.com? |  [Yes/No] | 
| Can you access Google.com from a browser? | [Yes/No] |
| What is the IP address of this host? |   | 


### Firewall setup
Now, we will finalise the configuration of the firewall. Log into the firewall from the Ubuntu host on the Private zone with:

```
http://10.10.x.254
```

Username: admin, Password: pfsense

Setup the required IP on the DMZ (10.10.y.254) and subnet mask.




# Appendix
User logins: 

Ubuntu:- User: napier, Password: napier123  
Kali:-  User: root, Password: toor  
Windows:-		User: Administrator, Password: napier123  
pfsense:- User: admin, Password: pfsense  
Metasploitable:- User: msfadmin, Password: napier123  


