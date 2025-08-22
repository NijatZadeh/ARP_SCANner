banner = r"""
        .-"      "-.
       /            \
      |,  .-.  .-.  ,|
      | )(_o/  \o_)( |
      |/     /\     \|
      (_     ^^     _)
       \__|IIIIII|__/
        | \IIIIII/ |
        \          /
         `--------`

      [ ARP  SCANNER ]
"""

print(banner)

from scapy.all import ARP, Ether, srp 

target = "TARGET_IP/CIDR" #EXAMPLE: "192.168.100.1/24"

arp = ARP(pdst=target) 
ether = Ether(dst="ff:ff:ff:ff:ff:ff") #UNIVERSAL BROADCAST

packet = ether/arp  
result = srp(packet, timeout=2, verbose=0)[0] 

for sent, received in result:
	print(f"IP: {received.psrc} MAC: {received.hwsrc}")

#yazilan kod - lokal sebekede olan butun cihazlarin ip ve mac
#unvanlarini gostermek ucun istfade edilir...

#received.psrc - gonderenin ip unvani
#receive.hwsrc - gonderenin mac unvani

#sebekede butun cihazlari tapmaq ucun ff:ff:ff:ff:ff:ff yaziriq

#==========================ArpScan===============================
