import scapy.all as scapy

packet = scapy.ARP(pdst="192.168.47.157",hwdst=" 3c:91:80:4f:ee:13",op=2,psrc="192.1168.47.147")

#print(scapy.ls(scapy.ARP()))
