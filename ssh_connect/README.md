# Interactive SSH Shell

A Python script to securely connect to a remote server via SSH and provide an interactive shell session.

## Introduction

This script allows to connect to a server using SSH, providing an interactive shell where user can run commands just like a normal SSH session. It supports both password and key-based authentication.

## Features

- Interactive Shell: Run commands interactively after connecting.
- Password & Key Auth: Supports both password and SSH key authentication.
- Local & Remote: Works for both local (`localhost`) and remote servers.
- Graceful Error Handling: Handles common SSH errors and connection issues.
- No Hardcoded Passwords: Prompts for password if not provided.

## Usage

### Prerequisites

- Python 3.x
- `paramiko` library (install with `pip install paramiko`)

### Running the Script

1. Save the script as `ssh_shell.py`.
2. Run the script:
   - For password-based auth:
     ```bash
     python ssh_shell.py <Server IP> username
     ```
   - For key-based auth:
     ```bash
     python ssh_shell.py <Server IP> username --key ~/.ssh/id_rsa
     ```
   - For custom port:
     ```bash
     python ssh_shell.py <Server IP> username --port 2222
     ```

### Output

- On successful connection, user will see 'Connected to localhost. Starting interactive shell. Type "exit" to quit.'
- On Failure, user will see 'SSH connection failed: {Exception}'
- On Socket connection Failure, user will see 'Socket error: {Error}'

## License

This project is licensed under the **MIT License**. Feel free to use, modify, and distribute it as needed.


