#!/usr/bin/env python

import scapy.all as scapy
import optparse

def scan():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="ip_address", help="Target IP address")

    (options, args) = parser.parse_args()

    arp_request = scapy.ARP(pdst=options.ip_address) #Making an ARP packet
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    arp_request_broadcast = broadcast / arp_request
    # scapy.ls(scapy.Ether())
    # print(arp_request_broadcast.summary())
    # print(arp_request_broadcast.show())

    # answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1)

    answered_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0]
    # print(answered_list.summary())
    # print("----------------------------------------------")
    # print(unanswered_list.summary())

    clients_list = []
    for element in answered_list:
        client_dict = {"ip":element[1].psrc, "mac":element[1].hwsrc}
        clients_list.append(client_dict)
        #print(element[1].psrc + "\t\t" + element[1].hwsrc)
    return clients_list

def print_clients(clients_list):
    print("---------------------------------------------------------------")
    print("IP\t\t\tMAC Address")
    print("---------------------------------------------------------------")
    for client in clients_list:
        print(client["ip"] + "\t\t" + client["mac"])

scan_result = scan()
print_clients(scan_result)