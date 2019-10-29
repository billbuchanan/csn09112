<img src="https://github.com/billbuchanan/csn09112/blob/master/zadditional/top_csn09112.png"/>

# CSN09112 - Network Security and Cryptography
This page provides an overview of the coursework [PDF][Download Bot]

## Outline Requirements

Botnets are a particular problem, where bot agents may infect machines inside an organisation’s network and connect back to a botnet controller out on the Internet, to receive commands and undertake malicious activities. The focus of this coursework is to create a virtualized testbed environment to analyse a particular botnet agent and the communications to its controller, to create and test a detection system to detect its activities, and then to mitigate its use in future with some firewall based defences.

* Configure a working perimeter network topology with a firewall, DMZ, and host systems as a testbed for the coursework. Secure the VMs by changing login passwords.
* Analyse the operation of the running Bot agent and Botnet controller, including any network scanning by the bot, activity on the host, network connections created, and any communications between the bot and controller.
* Create and test a detection system for the Botnet agent and controller using an IDS sensor.
* Create a closed perimeter, firewall policy configuration to prevent future communications for this particular botnet, but allow certain valid traffic, specified in next section.

Your network architecture similar to that shown in Figure 1 should be created with the VMs provided using two private address spaces, which you will be assigned on Moodle specifically for the coursework. The Bot agent should be run from the internal trusted Private network.

Start by allowing all traffic from the internal network out to the external network so the bot can communicate with the bot controller. Then use this architecture to investigate and analyse the Botnet activity and design a simple Intrusion Detection System (IDS) which will detect the various bot activity. Then implement a prototype using a Snort sensor running on the internal Linux system. The alerts generated should be useful to a security admin. Once the IDS has been tested, design and create firewall rules to close down the firewall to prevent future botnet activity, possibly highlight/log specific botnet activity, and test the configuration. Create a basic perimeter firewall solution, based around the current topology to provide a public web server from the external network, and Internet access from the internal network.

[Figure 1](https://asecuritysite.com/botnet.png)

## Demo

The following provides an overview of the task:

Snort should be installed within Kali, and is run with:

snort -c 1.rules -i eth0 -l log

When you are running the botnet, first note the IP address of the controller, and then run it:

mono bot.exe

A sample rules file has been placed in the instance. A good method of analysis is to get the PCAP fo the communication and then use Snort in an offline mode.

## Marking schedule

The coursework should be submitted via Turnitin (submit.ac.uk), in a PDF format, if possible. The hand-in date is 11:55pm on 18 Decemember 2019. It will be marked as follows:

* Requirements Analysis [20%]. This should show the analysis related to the main requirements, and an outline of the Web system, with the main design features. This should also include an analysis of the Bot, and how it can be detected.
* Botnet Analysis [40%]. This should outline the results of the evaluation of the Botnet agent and the controller.
* Outline implementation and Testing [30%]. This should define an outline implementation of the system which demonstrates the key implementation elements of the proposed system.
* References/Presentation [10%]. All references must be defined in an APA/Harvard format, and should be integrated in the report.

The report should use the APA/Harvard format for all of the references, and, if possible, should include EVERY reference to material sourced from other places. Also, the report should be up to 20 pages long (where appendices do not count in the page count number). 
