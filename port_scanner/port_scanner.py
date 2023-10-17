import socket
import asyncio
from tqdm import tqdm


def get_service_name(port: int) -> str:
    """
    Get the name of the service associated with a port.
    This function attempts to retrieve the name of the service associated with a port.
    If the service name is not found, it returns "Unknown."
    Args: port (int): The port number to identify the service for.
    Returns: str: The name of the service associated with the port.
    """

    try:
        service_name = socket.getservbyport(port)
    except OSError:
        service_name = "Unknown"
    return service_name


async def detect_open_ports(target_host, target_ports, max_concurrent=1000):
    """
    Asynchronously detect open ports on the target host and list the corresponding services,
    with a time limit of 1 second per port.
    This function scans a range of ports on the target host to check if they are open
    and identifies the associated services using asyncio.
    Args:   - target_host (str): The target host's IP address or hostname.
            - target_ports (list): List of ports to scan.
            - max_concurrent (int): Adjust this value to control concurrency
    Returns: List[str]: A list of messages indicating which ports are open and their associated services.
    """

    # check if ports are valid
    target_ports = [port for port in target_ports if port in range(1, 65537)]

    if len(target_ports) >= 1:
        print(f"Start scan of {len(target_ports)} ports.")
    else:
        print("all target ports are outside the valid range.")

    # Create a semaphore to control the maximum number of concurrent scans
    semaphore = asyncio.Semaphore(max_concurrent)
    open_ports = []

    # Define a function to scan a single port with a 1-second timeout
    async def scan_port(port, progress_bar):
        async with semaphore:
            try:
                # Use asyncio.wait_for to set a 1-second timeout for this scan
                result = await asyncio.wait_for(scan_port_with_timeout(target_host, port), timeout=1)
                if result:
                    open_ports.append(result)
            except asyncio.TimeoutError:
                pass
            except PermissionError:
                print(f"Port {port} requires administrative privileges and could not be scanned.")
            progress_bar.update()

    # Define a function to scan a single port with a timeout
    async def scan_port_with_timeout(target_host, port):
        try:
            # Attempt to open a connection to the target host and port
            reader, writer = await asyncio.open_connection(target_host, port)
            writer.close()
            await writer.wait_closed()
            return f"Port {port} is open. Service: {get_service_name(port)}"
        except (ConnectionRefusedError, TimeoutError):
            return None

    # Create a tqdm progress bar
    progress_bar = tqdm(total=len(target_ports), unit="port", unit_scale=True, dynamic_ncols=True, position=0)

    await asyncio.gather(*(scan_port(port, progress_bar) for port in target_ports))
    progress_bar.close()  # Close the progress bar

    return open_ports


if __name__ == "__main__":
    target_host = "localhost"  # Change this to the target host's IP address
    target_ports = range(1, 65536)  # You can specify the range of ports to scan

    open_ports = asyncio.run(detect_open_ports(target_host, target_ports))

    for result in open_ports:
        print(result)

