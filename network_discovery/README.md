# Network Device Discovery Script

The Network Device Discovery Script is a Python tool that allows you to discover devices on your local network using ARP requests.

## Usage

To use the Network Device Discovery Script, follow these steps:

1. Make sure you have the `scapy` library installed. You can install it using pip:

   ```commandline
   pip install scapy
   ```
2. Install `Npcap` from https://npcap.com/#download and install it.

3. Import the library in your Python script.

   ```commandline
   import network_discovery
   ```

4. Use the `scan` function to scan the devices in a ip range:

   ```python
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
   ```

5. Modify the `target_ip_range` variable with the desired IP range to scan.

6. Run your Python script to perform the network device discovery:

   ```commandline
   python discover_devices.py
   ```

7. The script will display the discovered devices' information, including their IP and MAC addresses.

## Dependencies
- `Npcap`: https://npcap.com/
- `scapy`: https://scapy.net/