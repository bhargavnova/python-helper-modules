# File Encryption Decryption Module

This is a Python module for file encryption and decryption using a password-based approach. It leverages the `cryptography` library to provide a simple and secure way to protect your files.

## Installation

To use this module, you need to install the required dependencies. You can do this using `pip` and the provided `requirements.txt` file:


## Usage

1. Import the `FileEncryptor` class from the module.

2. Create an instance of `FileEncryptor`.

3. Set the password for encryption and decryption using the `set_password` method.

4. Use the `encrypt_file` method to encrypt a file. The original file will be deleted after encryption.

5. Use the `decrypt_file` method to decrypt a file. The `.enc` file will be deleted after decryption.

Here's an example of how to use the module:

```python
from file_encryptor import FileEncryptor

encryptor = FileEncryptor()

# To set a password
password = "my_secure_password"
encryptor.set_password(password)

# To encrypt a file
encryptor.encrypt_file('file_encryption_decryption/example.txt')

# To decrypt the file
encryptor.decrypt_file('file_encryption_decryption/example.txt.enc')