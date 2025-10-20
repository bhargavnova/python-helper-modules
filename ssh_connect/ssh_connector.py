import paramiko
import getpass
import socket

def ssh_interactive_shell(hostname, username, password=None, key_filepath=None, port=22):
    """
    Start an interactive SSH shell session.

    Args:
        hostname (str): Server IP or domain (use 'localhost' for same PC).
        username (str): SSH username.
        password (str, optional): SSH password. If not provided, will prompt.
        key_filepath (str, optional): Path to private key file for key-based auth.
        port (int, optional): SSH port. Defaults to 22.
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        if key_filepath:
            # Key-based authentication
            private_key = paramiko.RSAKey.from_private_key_file(key_filepath)
            client.connect(hostname, port=port, username=username, pkey=private_key)
        else:
            # Password-based authentication
            if not password:
                password = getpass.getpass(f"Enter SSH password for {username}@{hostname}: ")
            client.connect(hostname, port=port, username=username, password=password)

        print(f"Connected to {hostname}. Starting interactive shell. Type 'exit' to quit.")

        # Start an interactive shell session
        shell = client.invoke_shell()
        while True:
            command = input("$ ")
            if command.lower().strip() in ["exit", "quit"]:
                break
            shell.send(command + "\n")
            while not shell.recv_ready():
                pass
            output = shell.recv(4096).decode()
            print(output, end="")

    except paramiko.AuthenticationException:
        print("Authentication failed. Check credentials.")
    except paramiko.SSHException as e:
        print(f"SSH connection failed: {e}")
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()
        print("🔌 Connection closed.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Interactive SSH Shell")
    parser.add_argument("hostname", help="Server IP or domain (use 'localhost' for same PC)")
    parser.add_argument("username", help="SSH username")
    parser.add_argument("--key", help="Path to private key file", default=None)
    parser.add_argument("--port", type=int, help="SSH port", default=22)
    args = parser.parse_args()

    ssh_interactive_shell(args.hostname, args.username, key_filepath=args.key, port=args.port)

