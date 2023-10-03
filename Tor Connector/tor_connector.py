import requests

# Base URL for checking if connected to Tor
TOR_CHECK_URL = "https://check.torproject.org/"

# Base URL for fetching the current IP address
IP_CHECK_URL = "https://httpbin.org/ip"


def connect():
    """Establishes a connection over the Tor network."""
    # Set up the session to use the Tor network
    session = requests.session()
    session.proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
    }
    
    try:
        # Test the connection
        response = session.get(TOR_CHECK_URL)
        if "Congratulations" in response.text:
            print("Successfully connected to the Tor network!")
            return session
        else:
            print("Failed to connect to the Tor network.")
            return None
    except requests.RequestException:
        print("Error while connecting to the Tor network.")
        return None


def get_ip(session=None):
    """Fetches the current IP address."""
    try:
        if session:
            response = session.get(IP_CHECK_URL)
        else:
            response = requests.get(IP_CHECK_URL)
        return response.json()["origin"]
    except requests.RequestException:
        print("Error while fetching the IP address.")
        return None


def verify_ip_change(session):
    """Verifies if the IP address has changed after connecting to the Tor network."""
    original_ip = get_ip()
    tor_ip = get_ip(session)
    
    return original_ip != tor_ip

# The script can be tested as is, but the idea is to use this as a module in other scripts.
