## Config 1
```
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
```

## Config 2
```
set zone-policy  zone  private  description  "Inside"
set zone-policy  zone  public  description  "Outside"
set zone-policy  zone  dmz description  "DMZ"

set zone-policy  zone  public  interface  eth0
set zone-policy  zone  private interface  eth1
set zone-policy  zone  dmz  interface  eth2

set firewall  name  dmz2private description  "DMZ to private"
set firewall  name  dmz2private rule  1  action  accept
set firewall  name  dmz2private rule  1  state  established  enable
set firewall  name  dmz2private rule  1  state  related enable
set firewall  name  dmz2private rule  10  action  accept
set firewall  name  dmz2private rule  10  destination  port  80,443  
set firewall  name  dmz2private rule  10  protocol tcp

set firewall  name  private2dmz description  "private to DMZ"
set firewall  name  private2dmz rule  1  action  accept

set  zone-policy  zone  private from  dmz firewall  name  dmz2private
set  zone-policy  zone  dmz from  private firewall  name  private2dmz
```

## Config 3

```
set firewall  name  private2public description  "private to public"
set firewall  name  private2public rule  1  action  accept
set zone-policy  zone  public from  private firewall  name  private2public

set firewall  name  public2private description  "public to private"
set firewall  name  public2private rule  1  action  accept
set firewall  name  public2private rule  1  state  established  enable
set firewall  name  public2private rule  1  state  related enable
set zone-policy  zone  private from  public firewall  name  public2private
```
## Config 4

```
set firewall  name  private2public description  "private to public"
set firewall  name  private2public rule  1  action  accept
set zone-policy  zone  public from  private firewall  name  private2public

set firewall  name  public2private description  "public to private"
set firewall  name  public2private rule  1  action  accept
set firewall  name  public2private rule  1  state  established  enable
set firewall  name  public2private rule  1  state  related enable
set zone-policy  zone  private from  public firewall  name  public2private

```

