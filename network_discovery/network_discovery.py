import scapy.all as scapy


def scan(ip_range):
    # Create an ARP request packet to get the MAC address associated with an IP
    arp_request = scapy.ARP(pdst=ip_range)

    # Create an Ethernet frame to send the ARP request
    ether_frame = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast MAC address

    # Combine the Ethernet frame and ARP request
    arp_request_packet = ether_frame / arp_request

    # Send the packet and capture the response
    answered_list = scapy.srp(arp_request_packet, timeout=1, verbose=False)[0]

    # Store the discovered devices' information in a list of dictionaries
    devices_list = []

    for element in answered_list:
        device_info = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        devices_list.append(device_info)

    return devices_list
