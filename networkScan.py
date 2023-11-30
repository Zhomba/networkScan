import scapy.all as scapy
import re

ip_add = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

while True:
    ip_entered = input("\nEnter IP address and range that you want to scan: ")
    if ip_add.search(ip_entered):
        print(f"{ip_entered} is a valid IP range")
        break


arp_result = scapy.arping(ip_entered)