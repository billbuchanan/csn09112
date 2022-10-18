<img src="https://github.com/billbuchanan/csn09112/blob/master/zadditional/top_csn09112.png"/>


# CSN09112 - Network Security and Cryptography
Author: Bill Buchanan

## Running the bot and controller
You can download the Bot onto the Linux machine using:

```
wget 'https://github.com/billbuchanan/csn09112/blob/master/coursework/c.zip?raw=true'
mv c.zip?raw=true c.zip
unzip c.zip
```


Setup the controller to run on Linux, and the botnet to run on Windows. go to your Windows machine on the DMZ, and download the ZIP file. You can run the controller on our Linux machine with:</p>

```
mono controller.exe
```

The output should show the form of:

```
Bot Controller Version 5.0
```

Take a note of the IP address of the controller (W.X.Y.Z). Now go your Windows machine, and run:</p>

```
bot.exe W.X.Y.Z
```


```
Bot Version 4.0 - 2021/2022
Please run with bot w.x.y.z, where w.x.y.z is the address of your controller.
Version 4.0
```

The bot and the controller should connect to each other.

## Outline Requirements

Botnets are a particular problem, and where bot agents may infect machines inside an organisation’s network and connect back to a botnet controller that can receive commands and undertake malicious activities. The focus of this coursework is to create a virtualized testbed environment to analyse a particular botnet agent and the communications to its controller, and then to create and test a detection system to detect its activities. Tasks include:

* Analyse the operation of the running Bot agent and Botnet controller, including any network scanning by the bot, activity on the host, network connections created, and any communications between the bot and controller.
* Create and test a detection system for the Botnet agent and controller using an IDS sensor.
* Configure a working perimeter network topology with a firewall, DMZ, and host systems as a testbed for the coursework.  

Your network architecture similar to that shown in Figure 1 should be created with the VMs provided using two private address spaces. The Bot agent should be run from the internal trusted Private network.

Start by allowing all traffic from the internal network out to the external network so the bot can communicate with the bot controller. Then use this architecture as your testbed to thoroughly investigate and analyse the Botnet activity. Try to plan and be scientific in the experimental method you use and don’t simply run it once and report. Static analysis can then be used to compliment the dynamic analysis. After this, design an Intrusion Detection System (IDS) which will detect the various bot activities, leading to an implementation of a prototype using a Snort sensor running on the internal Linux system. The alerts generated should be useful to a security admin. If you have time investigate tuning the rules. Once the IDS has been tested, design and create firewall rules to close down the firewall to prevent future botnet activity, possibly highlight/log specific botnet activity, and test the configuration. Finally, the botnet can be tested within the vSoC environment.

![Figure 1](https://github.com/billbuchanan/csn09112/blob/master/coursework/cw01.png)

## Demo

The following provides an overview of the task [here](https://www.youtube.com/watch?v=94iEY0XxPM8).

Snort should be installed within Ubuntu, and is run with:

```
snort -c 1.rules -i eth0 -l log
```

When you are running the botnet, first note the IP address of the controller, and then run it:

```
mono bot.exe
```

A sample rules file has been placed in the instance. A good method of analysis is to get the PCAP fo the communication and then use Snort in an offline mode.

## Marking schedule

The coursework should be submitted via Turnitin (submit.ac.uk), in a PDF format, if possible. The hand-in date is 11:55pm on 18 Decemember 2019. It will be marked as follows:

**Research [20 marks]**

A brief literature review towards your botnet analysis method and IDS rule development, demonstrating an understanding of the topics and using research from a variety of quality sources (cited in the text). Try to include some critical analysis - for example strengths and weaknesses, justification, and highlighting findings which inform the later work - and possibly recent examples and how they were analysed.
<p align="right">[20 marks]</p>

**Botnet Analysis [40 marks]**

Configure a working perimeter network topology with a firewall, DMZ, and host systems as a testbed for the coursework. For example annotated network diagram, and some basic configuration/connectivity testing shown and discussed briefly.
Discuss methods informed from the research, and apply these to analyse the operation of the running Bot agent and Botnet controller, including any connections created by the bot, possible host activities on the victim, communications between the bot and controller, and other bot behaviour. For example, screen shots and brief discussion for: botnet components running, analysis tools, outputs and interesting data, tools and outputs of cracking codes, with brief discussion.
- Dynamic analysis of bot and botnet controller could include identifying botnet network connections and traffic, filtering out unrelated traffic using appropriate tools, identify types of traffic generated, identify specific botnet commands and responses, decoing botnet traffic if necessary. Challenge: create your own bot traffic so individual command can be sent and analysed separately. 

<p align="right">[40 marks]</p>

**Prototype Defenses Implementation and Testing [30 marks]**

Apply method from the research, which should define an outline prototype implementation of the defences.
- From your botnet analysis, create and test a basic prototype detection system for the Botnet agent and controller using an IDS sensor. Create IDS rules/signatures to detect the bot activity and not excessively many false positives. This section could show the Snort rules with descriptions of how they work, and screen shots of the testing/outputs and discussion on this.
- Create a closed perimeter firewall configuration to prevent/highlight future communications for this particular botnet, but allow certain valid traffic (specified in requirements spec’). Again show the configuration/rules and testing using screen shot snippets with brief explanation, and any discussion on the findings/outputs.
<p align="right">[30 marks]</p>

**References/Presentation [10 marks]**

The academic report should be written in a formal style, in 3rd person, and well presented.
Full academic referencing of peer reviewed papers, technical papers, books, and web sites, using thorough the Harvard referencing format.
- Reference all materials used, citing every reference in the body of the report.
- All references cited should be listed at the end of the report, using Harvard referencing format.
<p align="right">[10 marks]</p>

The report should use the Harvard format for all of the references, and, if possible, should include EVERY reference to material sourced from other places. Also, the report should be up to 20 pages long (where appendices do not count in the page count number). 

