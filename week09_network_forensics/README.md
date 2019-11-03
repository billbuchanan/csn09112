<img src="https://github.com/billbuchanan/csn09112/blob/master/zadditional/top_csn09112.png"/>
<h1 id="logo">Chapter 9: Network Forensics</h1>
<h2>Objectives</h2>
<p>[<a href="javascript:history.go(-1)">Back</a>] The key objectives of this chapter are:</p>
<ul>
  <li>Understand  some of the methodologies used in network forensics.</li>
  <li>Provide  an in-depth understanding of the key network protocols, including IP, TCP, ARP,  ICMP, DNS, Application Layer protocols, and so on.</li>
  <li>Define  a range of audit sources for network activity.</li>
</ul>
<h2>Lecture</h2>
  

    <p>The main lecture is here:</p>
<iframe width="560" height="315" src="//www.youtube.com/embed/9_u1eriQtSY?rel=0" frameborder="0" allowfullscreen></iframe>
    <h2>Test</h2>
<p>The test for this unit is <a href="/tests/tests?sortBy=sfc09">Test</a>.</p>
<h2>Network Forensics</h2>

    <ul>
      <li>  <a href="/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Fping.txt"> Network Forensics - Ping</a> </li>
     <li>  <a href="/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Ftelnet.txt"> Network Forensics - Telnet</a> </li>
   <li>  <a href="/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Fdnslookup.txt"> Network Forensics - DNS Lookup</a> </li>
   <li>  <a href="/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Fftp.txt"> Network Forensics - FTP</a> </li>
   <li>  <a href="/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Fnmap.txt"> Network Forensics - NMAP</a> </li>
   <li>  <a href="/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Ftracert.txt"> Network Forensics - Tracert</a> </li>
   <li>  <a href="/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Fwebpage.txt"> Network Forensics - Web page</a> </li>
   <li>  <a href="/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Fssl.txt"> Network Forensics - SSL</a> </li>
   <li>  <a href="/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Fspoof_address.txt"> Network Forensics - Spoof Address</a> </li>
    <li>  <a href="/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Fipsec.txt"> Network Forensics - IPSec</a> </li>
    <li>  <a href="/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2FgoogleWeb.txt"> Network Forensics - GoogleWeb</a> </li>
      <li>  <a href="/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Fpacket_ip_ub.txt"> Network Forensics - IP Packet (Windows)</a> </li>
         <li>  <a href="/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Fpacket_ip_windows.txt"> Network Forensics - IP Packet (Ubuntu)</a> </li>
          <li>  <a href="/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Fhydra_ftp.txt"> Network Forensics - Hydra traces: FTP</a> </li>
          <li>  <a href="/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Fhydra_telnet.txt"> Network Forensics - Hydra traces: Telnet</a> </li>
                  <li>  <a href="/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Fhping_fin.txt"> Network Forensics - Hping traces: hping_fin</a> </li>
                         <li>  <a href="/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Fhping_ping_scan.txt"> Network Forensics - Hping traces: hping_ping_scan</a> </li>
     <li>  <a href="/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Fhping_port80.txt"> Network Forensics - Hping traces: hping_port80</a> </li>
      <li>  <a href="/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Fhping_port80_fin.txt"> Network Forensics - Hping traces: hping_port80_fin</a> </li>
         <li>  <a href="/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Fhping_syn.txt"> Network Forensics - Hping traces: hping_syn</a> </li>
           <li>  <a href="/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Fhping_udp_scan.txt"> Network Forensics - Hping traces: hping_udp_scan</a> </li>
                  <li>  <a href="/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Fhping_udp_scan.txt"> Network Forensics - Hping traces: hping_udp_scan</a> </li>
                         <li>  <a href="/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Fhydra_ftp.txt"> Network Forensics - Hping traces: hydra_ftp</a> </li>
                                          <li>  <a href="/forensics/net?sortBy=video%3Aasecuritysite.com%2Flog%2Fhydra_telnet.txt"> Network Forensics - Hping traces: hydra_telnet</a> </li>
 </ul>
  <h2>Related Material</h2>
<ul>
     
     <li>  <a href="/information/videos?sortBy=video%3Abuchananweb.co.uk%2Fadv_security_and_network_forensics%2Ftcpdump01%2Ftcpdump01.htm">Network Forensics - TCPDump</a> This shows an example of analysing simple network traces. </li>
     <li>  <a href="/information/videos?sortBy=video%3Awww.youtube.com%2Fembed%2FMvMnwDeXvZo%3Fhd%3D1%3Frel%3D0">Tripwire</a> This shows an example of configuring Tripwire in Linux. </li>
     <li>  <a href="/forensics/pcap">Network Forensics - PCAP analysis</a> </li>
     
  
      </ul>
  
<h2>Lab</h2>
<p>The lab is [<a href="https://www.asecuritysite.com/public/lab07_network_forensics_protocols.pdf" target="_blank">here</a>]</p>

<h2>Slides</h2>

        <p>The slides for the chapter are [<a href="/book_chap08.pdf">here</a>] and the notes are [<a href="/public/unit09.pdf">here</a>]</p>

</td></tr>
</table>

<table width="100%" border="1" cellpadding="0" cellspacing="0"> 
<tr><td valign="top">
	
<h2>Introduction to IP/MAC Addresses</h2>
<p>This oulines the basic concepts of Routing and switching, along with IP and MAC address. The content is:</p>
          <ul>
       <li><strong>Slides</strong>. <a href="/dicontent/intro.pdf" target="_blank"> Slides</a></li>   
<li><strong>Test</strong>. <a href="/tests/tests?sortBy=d01_01"> Test</a>.</li>
<li><strong>Lab</strong>. <a href="/dicontent/lab01_01.pdf" target="_blank">Lab</a></li>
  
   </ul>

    <iframe width="420" height="315" src="//www.youtube.com/embed/kgrbM6NOrOg?rel=0" frameborder="0" allowfullscreen></iframe>
             <iframe width="420" height="315" src="//www.youtube.com/embed/PkdqvXXQjoA?rel=0" frameborder="0" allowfullscreen></iframe>


<h2>Lower-level protocols: Ethernet, IP and TCP</h2>
    <ul>
           <li><strong>Slides</strong>. <a href="/dicontent/day01_02.pdf" target="_blank"> Slides</a></li>   
<li><strong>Test</strong>. <a href="/tests/tests?sortBy=d01_02"> Test</a>.</li>
<li><strong>Lab</strong>. <a href="/dicontent/lab01_02.pdf" target="_blank">Lab</a></li>
  
   </ul>
     <iframe width="420" height="315" src="//www.youtube.com/embed/CGMtK4woT_I?rel=0" frameborder="0" allowfullscreen></iframe>

  
  <iframe width="420" height="315" src="//www.youtube.com/embed/FhVN-gZnQq0?rel=0" frameborder="0" allowfullscreen></iframe>

 <h2>High-level Protocols: HTTP, DNS, FTP</h2>
   <ul>
               <li><strong>Slides</strong>. <a href="/dicontent/day01_03.pdf" target="_blank"> Slides</a></li>   
<li><strong>Test</strong>. <a href="/tests/tests?sortBy=d01_03"> Test</a>.</li>
<li><strong>Lab</strong>. <a href="/dicontent/lab01_03.pdf" target="_blank">Lab</a></li>
  
   </ul>
<iframe width="420" height="315" src="//www.youtube.com/embed/C1NCH3S8NAQ?rel=0" frameborder="0" allowfullscreen></iframe>
<iframe width="420" height="315" src="//www.youtube.com/embed/l0A4Xrfq5Tc?rel=0" frameborder="0" allowfullscreen></iframe>
<h2>High-level Protocols: ARP and ICMP</h2>
   <ul>
               <li><strong>Slides</strong>. <a href="/dicontent/day01_04.pdf" target="_blank"> Slides</a></li>   
<li><strong>Test</strong>. <a href="/tests/tests?sortBy=d01_04"> Test</a>.</li>
<li><strong>Lab</strong>. <a href="/dicontent/lab01_04.pdf" target="_blank">Lab</a></li>
  
   </ul>

    <iframe width="420" height="315" src="//www.youtube.com/embed/xVXa2jk7CxM?rel=0" frameborder="0" allowfullscreen></iframe>
    <iframe width="420" height="315" src="//www.youtube.com/embed/T_jrAwZfE74?rel=0" frameborder="0" allowfullscreen></iframe>
    <h2>High-level Protocols: SMTP, IMAP and POP-3</h2>
   <ul>
               <li><strong>Slides</strong>. <a href="/dicontent/day01_05.pdf" target="_blank"> Slides</a></li>   
<li><strong>Test</strong>. <a href="/tests/tests?sortBy=d01_05"> Test</a>.</li>
<li><strong>Lab</strong>. <a href="/dicontent/lab01_05.pdf" target="_blank">Lab</a></li>
  
   </ul>

    <iframe width="420" height="315" src="//www.youtube.com/embed/1L4lKRMTzFM?rel=0" frameborder="0" allowfullscreen></iframe>
    <iframe width="420" height="315" src="//www.youtube.com/embed/3RHrq3EehsE?rel=0" frameborder="0" allowfullscreen></iframe>

        <h2>High-level Protocols: SSL and TLS</h2>
   <ul>
               <li><strong>Slides</strong>. <a href="/dicontent/day01_06.pdf" target="_blank"> Slides</a></li>   
<li><strong>Test</strong>. <a href="/tests/tests?sortBy=d01_06"> Test</a>.</li>
<li><strong>Lab</strong>. <a href="/dicontent/day01_06.pdf" target="_blank">Lab</a></li>
  
   </ul>
    <iframe width="420" height="315" src="//www.youtube.com/embed/whPgoZpsu6Y?rel=0" frameborder="0" allowfullscreen></iframe>
    <iframe width="420" height="315" src="//www.youtube.com/embed/jejjoSCn6Yg?rel=0" frameborder="0" allowfullscreen></iframe>
