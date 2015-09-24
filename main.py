import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *






print "[SCAPY] : Start a ICMP packet"
myPingTrame = Ether()/ IP(dst='192.168.1.24') / ICMP() #my other computer
ls(myPingTrame)
reply = srp1(myPingTrame)


print "[SCAPY] : Generate Basic IP/Ethernet packet"
ipTrame = Ether() / IP(dst='192.168.1.24')


print "[SCAPY] : Start a TCP packet"
TCPTrame = TCP()
TCPTrame.dport =8888 #dest port
TCPTrame.flags ="S"  #S = Syn
TCPTrame.sport =6789 #src port
TCPTrame.seq =69
TCPTrame.show()
reply = srp1(ipTrame / TCPTrame)
reply.show()
