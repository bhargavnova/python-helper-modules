# Usage
import tor_connector

session = tor_connector.connect()

ip_changed = tor_connector.verify_ip_change(session)

if ip_changed:
    print("IP address has changed.")
else:
    print("IP address remains the same.")
