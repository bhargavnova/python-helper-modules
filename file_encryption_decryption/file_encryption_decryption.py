import base64
import hashlib
from cryptography.fernet import Fernet
import os

class FileEncryptor:
    def __init__(self):
        self.password = None
        self.salt = b'my_constant_salt'  # Use a constant salt

    def set_password(self, password):
        self.password = password.encode('utf-8')

    def generate_key(self):
        if not self.password:
            print("Password is required.")
            return None

        key = hashlib.pbkdf2_hmac('sha256', self.password, self.salt, 100000, 32)
        return base64.urlsafe_b64encode(key)

    def encrypt_file(self, file_path):
        key = self.generate_key()
        if key is None:
            return

        fernet = Fernet(key)

        with open(file_path, 'rb') as input_file:
            file_contents = input_file.read()

        encrypted_contents = fernet.encrypt(file_contents)

        output_file_path = f"{file_path}.enc"

        with open(output_file_path, 'wb') as output_file:
            output_file.write(encrypted_contents)

        # Delete the original file after encryption
        os.remove(file_path)

    def decrypt_file(self, file_path):
        key = self.generate_key()
        if key is None:
            return

        fernet = Fernet(key)

        with open(file_path, 'rb') as enc_file:
            encrypted = enc_file.read()

        decrypted = fernet.decrypt(encrypted)

        # Generate the output file path with a .txt extension
        output_file_path = file_path[:-4]  # Remove the .enc extension

        with open(output_file_path, 'wb') as dec_file:
            dec_file.write(decrypted)

        # Delete the .enc file after decryption
        os.remove(file_path)

# Example usage
if __name__ == "__main__":
    encryptor = FileEncryptor()

    password = "my_secure_password"
    encryptor.set_password(password)

    # Encrypt a file
    encryptor.encrypt_file('example.txt')

    # Decrypt the file
    encryptor.decrypt_file('example.txt.enc')
