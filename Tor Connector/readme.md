# Tor Connector
A Python module to establish a connection over the Tor network and verify IP address changes.

# Prerequisites
Ensure you have Python 3.x installed.

Install the required Python packages:
```bash
pip install pysocks requests
```
Make sure you have the Tor service installed and running on your machine


# Features
- Tor Connection Setup: The module establishes a connection through the Tor network, ensuring anonymous browsing.

- IP Change Verification: The module provides a mechanism to confirm that the IP address has changed after connecting through Tor.

- User-Friendly Output: Provides clear feedback on the Tor connection status and IP address verification.

# Troubleshooting
If you face any issues related to proxy connections, it's usually related to the Tor service not running or not being accessible. Ensure that Tor is running and listening on port 9050 (or the port you configure) before using this module.