import network_discovery

if __name__ == "__main__":
    target_ip_range = "192.168.29.1/24"

    print("Scanning for devices on the network...")
    devices = network_discovery.scan(target_ip_range)

    if devices:
        print("Discovered devices:")
        for device in devices:
            print(f"IP: {device['ip']} | MAC: {device['mac']}")
    else:
        print("No devices found on the network.")
