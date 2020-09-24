<img src="https://github.com/billbuchanan/csn09112/blob/master/zadditional/top_csn09112.png"/>

# Unit 3: Network Security
## Objectives
The key objectives of this unit are:</p>

* Provide an overview of security devices and infrastructures.
* Provide an introduction to key network security devices including proxy servers, and firewalls.

## Test
The test for this unit is [here](https://asecuritysite.com/tests/tests?sortBy=sfc06).

There is a fun test at [here](https://asecuritysite.com/tests/fun?sortBy=sfc06).

## Slides
<p>The slides for the chapter are [here](https://github.com/billbuchanan/csn09112/blob/master/week03_ns/lecture/unit03_nets.pdf).

## Additional
Snort analyser: <a href="https://asecuritysite.com/forensics/snort2">here</a>

VMRC 11.x can be forced to run in legacy mode, which should work with current IS firewall configuration. I’d say this is probably the best workaround to suggest:
Configure VMware Remote Console 11.x to use the legacy connection mode. To do so, open the VMware preferences file on the host machine and add the following parameters:

```
pref.preferWebMKS = "FALSE"
pref.preferWebRemoteDevice = "FALSE"
```

The preferences file can be found in the following location:

* Windows: %APPDATA%\VMware\preferences.ini
* macOS (standard install): ~/Library/Preferences/VMware Remote Console/preferences
* macOS (App Store install):~/Library/Containers/com.vmware.vmrc/Data/Library/Preferences/VMware Remote Console/preferences
* Linux: ~/.vmware/preferences

Passwords:

```
Vyatta. User: vyatta, Password: vyatta
Windows 2003: User: Administrator, Password: napier
Ubuntu: User: root, password: napier123
Kali: User: root, password: toor
```

Software:

* VMWare Fusion or Workstation: https://softcentre.soc.napier.ac.uk/users.cgi
* VPN: https://napier-sslvpn.napier.ac.uk/




