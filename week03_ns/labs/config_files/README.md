<p>Config 1</p>
<pre>
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
</pre>