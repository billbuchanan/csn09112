<img width="1086" height="214" alt="image" src="https://github.com/user-attachments/assets/e41a66b6-5370-4c19-86ab-dc124b896eeb" />

# Lab 2: Creating Secure Architectures

## Aim
The aim of this  lab is to build a secure architecture.

## Activities

Complete Lab 2: The lab is [here](https://github.com/billbuchanan/csn09112/blob/master/week03_ns/labs/csn09112_lab02.pdf) and there a demo of the lab [here](https://www.youtube.com/watch?v=g7dzDM4aU0k).</p>


## Lab setup
Our challenge is to setup MyBank Incorp, where each of you will be allocated a network and hosts to configure and get on-line (Figure 1). You have a pfSense firewall, a Ubuntu (Private) host, a Windows (DMZ) host, a Metasploitable (DMZ) host and a Kali (DMZ) host to achieve your objectives. 

<img width="2658" height="1028" alt="image" src="https://github.com/user-attachments/assets/7798f13f-276e-49d4-a452-24d53fbe6ab6" />

Figure 1: Lab setup (em0 – Public, em1 – Private, em2 – DMZ) 

In Moodle, click on Virtual Labs (CSN09112) and open up [here](https://moodle.napier.ac.uk/mod/lti/view.php?id=3055667):

<img width="1810" height="981" alt="image" src="https://github.com/user-attachments/assets/ebcc8ba4-6865-4aaa-9e0f-2a42f3fbc0f4" />

Select “Cyber Modular Labs”, and then select the project “bill_csn09112.gns”:

<img width="2246" height="1008" alt="image" src="https://github.com/user-attachments/assets/9540c908-35b3-477d-a0f3-62e7d28c18d6" />

The setup for GNS3 is:

<img width="1828" height="1084" alt="image" src="https://github.com/user-attachments/assets/22ac0fe0-d99f-4789-9b54-0b4e99c8a3fb" />

### Firewall  set up
On the firewall, from Diagnostics, view the ARP cache. Which addresses are in the cache?

On the firewall, from Diagnostics, ping each of the 192.168.10.254 and 192.168.10.7 interfaces from the LAN network. Can you ping them? [Yes/No]


On the Windows host, ping the 192.168.11.254 and 192.168.11.7 interfaces. Can you ping them? [Yes/No] Why can’t you ping the 192.168.11.254 interface?



On the firewall, create a rule which allows a host on the DMZ to use ICMP to any destination.

On the Windows host, ping 192.168.11.254 and 192.168.11.7 interfaces. You should now be able to ping them.

On the Windows host, ping 192.168.10.254 and 192.168.10.7 interfaces. You should now be able to ping them.

On the firewall, create a rule which allows the Public network to ping both the DMZ and Private network. From the firewall, can you ping the hosts in the DMZ and Private network from the WAN port? The answer should be no, as the routing has not been set yet.

Now from the Windows host and the Ubuntu host, ping all the key addresses, including the gateway 10.221.3.254.


### NAT
Now we will investigate NAT on the device.

Run packet capture on the firewall, and then ping from both the Windows host and the Ubuntu host. Stop the trace.

Which IP address appears in the pings? 

Why is it just a single address?



### Routing table
Now we will investigate the routing table on the firewall.

On the firewall, investigate the firewall, and identify how the device makes decisions on the routing of data packets. What is the default gateway?





Now we will investigate the Metasploitable host.

Run NMAP from Windows to Metasploit. Which services are enabled:

[ftp][ssh][telnet][smtp][domain][http][vnc]

Run NMAP from Ubuntu to Metasploit. Which services are enabled:

[ftp][ssh][telnet][smtp][domain][http][vnc]

Now we will investigate the Metasploitable host for Telnet:

From Windows, run Wireshark and capture packets. Now log into Metasploitable using telnet:
```
telnet 192.168.11.9
```
Can you log into each into Metasploit: [Yes/No]

Stop Wireshark and examine the data packets. Can you find the Telnet login session, and can you discover the password used? [Yes/No]

From Ubuntu run Wireshark and capture packets. Now log into Metasploitable using telnet:
```
telnet 192.168.11.9
```
Can you log into each into Metasploit: [Yes/No]

Stop Wireshark and examine the data packets. Can you find the Telnet login session, and can you discover the password used? [Yes/No]

Note: login for Telnet in Metasploitable is User: msfadmin, Password: napier123

Now we will investigate the Metasploitable host for Telnet:

From Windows, run Wireshark and capture packets. Now log into Metasploitable using SSH:
```
ssh 192.168.11.9 -l msfadmin
```
Can you log into into Metasploit: [Yes/No]

Stop Wireshark, and examine the data packets. Can you find the Telnet login, and can you discover the password used? [Yes/No]

From Ubuntu, run Wireshark and capture packets. Now log into Metasploitable using SSH:
```
ssh 192.168.11.9 -l msfadmin
```
Can you log into Metasploit: [Yes/No]

Stop Wireshark and examine the data packets. Can you find the SSH login session, and can you discover the password used? [Yes/No]

Note: in Wireshark, use tcp.port==23 as a filter for Telnet and use tcp.prt==22 as a filter for SSH.




## D	Device Audit
Now we will make sure everything is in order with our infrastructure, such as for testing for network traffic, MAC addresses and so on. Audit list:

| Perform and answer the following: |
|-------------------------------|
| On the firewall, capture traffic on the DMZ port, and generate some traffic from the LAN to the DMZ (such as accessing the Web server in the DMZ).  Does the traffic have the IP address of the gateway on the LAN port? Tick [ ]
| On the firewall, capture traffic on the WAN port, and generate some traffic from the LAN and DMZ (such as accessing Google.com).  Does the traffic have the IP address of the WAN port? Tick [ ]
| On the firewall, examine the ARP table. Also on the hosts in the DMZ and the LAN, run arp –a, and determine all your MAC addresses.  Do all the MAC addresses tie up? Tick [ ]

## E	NMAP
Run Wireshark on both hosts. Now run NMAP from the Linux host to the Windows host, and from the Windows host to the Linux host.

| Perform and answer the following: |
|-------------------------------|
| What IP addresses are used in the source addresses of the scan?
| Which services have been identified from the Linux host to the Windows host?
| Which services have been identified from the Windows host to the Linux host?
| Why are these different in their scope? Where is the blocking happening?


Now enable http (Port 80), https (Port 443), and ftp (Port) from the Private network to the DMZ.

| Perform and answer the following: |
|-------------------------------|
| Re-do NMAP. How are the scans different?
| Can you now access the Web server from the Linux host to the Windows host?
| Can you now access the Web server from the Windows host to the Linux host?


Access Google.com from the Ubuntu host and also the Windows host.

| Perform and answer the following: |
|-------------------------------|
| Can you access it? If not, on the firewall, enable UDP/TCP DNS (Port 53) from DMZ and also from the Private network. Add logging on the rule.
| Can you now access Google.com from the Linux host and the Windows host?
| On the firewall, examine the log and view the accesses for a DNS lookup on Google.com. Which addresses are present?



## F Identifying Services 
Within a network infrastructure, we have services which run on hosts. These services provide a given functionality, such as for sending/receiving email, file storage, and so on.

| From → To |	Command	| Observation |
|------|------------|-------------|
| DMZ	| On your Windows host, run the command: netstat –a and outline some of the services which are running on your host (define the port number and the name of the service and only pick off the LISTENING status on the port).	| Outline some of the services which are running on your host (define the port number and the name of the service): |
| LAN		| For the Ubuntu Virtual Machine, and run the command: netstat –l.  	| 	Outline some of the services which are running on your host (define the port number and the name of the service):	| 
| DMZ		| Next we will determine if these services are working. There should be a Web server working on each of the virtual machines (Ubuntu and Windows 2003), so from the Windows host and using a Web browser, access the home page: http://192.168.10.7		|  Is the service working: [Yes] [No] 	| 
|  LAN	|  From Ubuntu, access the Web server at: http://192.168.11.7	| Is the service working: [Yes] [No]| 
| LAN	|  Next we will determine if these services are working using a command line. From your UBUNTU host, undertake the following: telnet 192.168.11.7 80 then enter:  GET / | 	Outline the message that is returned: | 
| DMZ	|  Repeat the previous example from the WINDOWS host: telnet 192.168.10.7 80	|  
| DMZ	|  There should be an FTP server working on Ubuntu and Windows 2003. From WINDOWS, access the FTP server on the UBUNTU server: "telnet 192.168.10.7 21"  then enter: "USER napier" then "PASS napier123" and then "QUIT" | 	Outline the messages that you received: What happens to each of these when you try with an incorrect username and password:  | 
| LAN | 	From UBUNTU access the WINDOWS host with "telnet 192.168.10.7 21" then enter: "USER Administrator" then "PASS napier" and then "QUIT" | 	Outline the messages that you received: What happens to each of these when you try with an incorrect username and password: | 
| DMZ	| On the UBUNTU instance you will see that the VNC service is running, which is the remote access service. From your WINDOWS host, access the VNC service using a VNC client, and see what happens (you may have to open up Port 5900 to do so). |  What does this service do: | 





## G	Enumeration – Host scan 

Nmap is one of the most popular network scanning tools. It is widely available for Windows and Linux/Unix platforms, and has both a Command Line Interface (CLI) and a Graphical User Interface (GUI).  

| From → To |	Command	| Observation |
|------|------------|-------------|
| LAN to WAN|	sudo nmap –sP –r 10.221.0.0/24	|Which hosts are on-line:| 
| LAN to DMZ|	sudo nmap –sP –r 192.168.11.0/24|	Which hosts are on-line:| 
| DMZ to LAN	|nmap –sP –r 192.168.10.0/24|	Which hosts are on-line:| 
| LAN to DMZ|	Run Wireshark on host in LAN, and run: sudo nmap –sP –r 192.168.11.0/24|	Which transport layer protocol does NMAP use to discover the host: [ICMP] or [ARP]| 
| LAN to LAN|	Run Wireshark on host in LAN, and run: sudo nmap –sP –r 192.168.10.0/24|	Which transport layer protocol does NMAP use to discover the host: [ICMP] or [ARP]| 

## H	Enumeration - Operating System Fingerprinting
Enumeration is the gathering of information about target hosts. After discovering live target systems, we want to identify which machines are running which OSs. A useful feature of nmap, is determining the operating system of hosts on the network. It performs active OS fingerprinting by sending packets to the target system. 

| From → To |	Command	| Observation |
|------|------------|-------------|
|LAN to DMZ	| Perform an OS Fingerprint Scan on some of the hosts discovered on the network, using a command such as: sudo nmap –O 192.168.11.0/24 |  Which operating systems does it return: |
|DMZ to LAN	|Perform an OS Fingerprint Scan on some of the hosts discovered on the network, using a command such as: nmap –O 192.168.10.0/24	| Which operating systems does it return: |

## I	Enumeration – Application Fingerprinting
Application Fingerprinting or Banner Grabbing covers techniques to enumerate OSs and Applications running on target hosts. An attacker or security tester would be specifically looking for versions of applications and operating systems which have vulnerabilities. Nmap can be used to check applications and versions for network services running on the target for the open ports it finds during a port scan. 

| From → To |	Command	| Observation |
|------|------------|-------------|
|LAN to DMZ	| Perform an application and version scan for networked services: sudo nmap –sS 192.168.11.7/24 | Which services are running on the Windows host:|
|DMZ to LAN	Perform an application and version scan for networked services: nmap –sS 192.168.10.7/24 | Which services are running on the Linux host:|
|LAN to DMZ	|Scan the Web server in the DMZ for its version:  sudo nmap –sV 192.168.11.7/24 –p 80	| Which Web server type is being used:|
| DMZ to LAN	| Scan the Web server in the LAN for its version: nmap –sV 192.168.10.7/24 –p 80 | Which Web server type is being used:|


Telnet is another tool commonly used for banner grabbing. Once open ports have been found using a scanner, Telnet can be used to connect to a service and return its banner.

| From → To |	Command	| Observation |
|------|------------|-------------|
| DMZ to LAN	| Connect to port 80, with: telnet 192.168.10.7 80 and then send the HTTP OPTIONS command to the web server: OPTIONS / HTTP/1.0 | What is returned and how can this be used to fingerprint the web server? Which web server is running and which version? |
| DMZ to LAN	| Similarly, other HTTP commands such as HEAD (get an HTML page header) and GET (get the whole HTML page) can be used to footprint a web server. Try the following and observe: HEAD / HTTP/1.0 and GET / HTTP/1.0	| What do you observe from using these HTTP requests:| 


## J	Brute Force
For this part of the lab, we will crack the username and password on the FTP login on Metasploitable. We will on Kali (DMZ), where you create a user file and password file with the following lists:

list_user: 
* administrator
* admin
* root
* msfadmin
* guest

list_password:

* adminpass
* password
* Password
* 123456
* napier123
* pa$$word

Next, start Wireshark on Kali (DMZ), and then run Hydra with these usernames and passwords:

```
# hydra -L list_user -P list_password 192.168.11.9 ftp
```

From this, determine one of the usernames and passwords.


Stop Wireshark and find the Hydra trace. What do you observe from the trace:


What is the FTP status code for an incorrect login:


What is the FTP status code for a correct login:

<!--- Ensure you have snort installed by running `snort -h`. --->
<!---If you have installation issues, run a `sudo apt-get update` first.

Now write a Snort rule to detect an incorrect login on FTP (and thus detect a possible Hydra scan on the server). Hint: you need to detect “530” in the Port 21 connection.

Which rule have you used:


Rerun Hydra and start Snort to detect incorrect logins. Did it detect the scan? [Yes/No] --->


Next, run Hydra and crack the username and the password for the Web server. With these usernames and passwords, we will target the DVWA site. First, access the Web server from:

```
http://192.168.11.9/dvwa/login.php
```
Next, start Wireshark on Kali (DMZ), and then run Hydra to try a range of logins:

```
# hydra -L list_user -P list_password 192.168.11.9 http-post-form ‘/dvwa/login.php:username=^USER^&password=^PASS^&Login=Login:Login failed’
```
From this, determine one of the usernames and passwords.


Stop Wireshark and find the Hydra trace. What do you observe from the trace:


What is the HTTP status code for an incorrect login:


What is the HTTP status code for a correct login:


Now access the Mutillidae site on Metasploit:
```
http://192.168.11.9/mutillidae
```
Now we will attack the Mutillidae site:
```
# hydra -L list_user -P list_password 192.168.11.9 http-post-form 
'/mutillidae/index.php?page=login.php:username=^USER^&password=^PASS^&login-php-submit-button=Login:Not Logged In'
```
From this, determine one of the usernames and passwords.

## K	NAT and 1:1 mappings

No other group can access any of your hosts, as you are behind NAT. Now we need to set up a 1:1 mapping and a virtual IP address (with Proxy ARP) to map an internal address to an external one. First, we need to find an IP address from the 10.221.0.0/22 network which is not being used, and then we will use this to allow other groups’ access to the hosts in the DMZ (Figure 2).

Demo: https://youtu.be/1wn2io8EWvs 

<img width="940" height="497" alt="image" src="https://github.com/user-attachments/assets/1d1be93f-3d32-49bf-b77d-f83b30ad34c2" />

Figure 2: Setup 1:1 NAT for mapping of servers 

Run NMAP from the Private network with: nmap –sP 10.221.0.0/24

Which hosts are online?

Now pick an address which is (where GROUP ID is the third digit of your private network address), eg if your private address is 10.10.43.0, then set up the address of 10.221.2.43:

10.221.2.[GROUP ID]

Now, on the firewall, set up a 1:1 mapping of the External IP address that you have selected and the Internal IP address on the DMZ (Figure 3).

Next, set up a Virtual IP address (with Proxy ARP) for the external address you have selected, which will advertise the IP address (Figure 4).

Now from the WAN interface, ping the host in the DMZ. Can you ping it?

Finally ask, someone in another group to ping your host in the DMZ. Can they ping it?

Now get them to access the Web server on your host.

Finally get them to NMAP your host? What can you observe from the NMAP?

<img width="732" height="269" alt="image" src="https://github.com/user-attachments/assets/13e5df20-49d2-47f9-aa0a-cbf4bfcd5a88" />

Figure 3: 1:1 NAT settings

<img width="646" height="222" alt="image" src="https://github.com/user-attachments/assets/2966fa30-08ec-460f-bb3c-28a0ad0bc306" />

Figure 4: Virtual IP addresses


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


