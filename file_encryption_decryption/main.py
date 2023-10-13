from file_encryption_decryption import FileEncryptor

if __name__ == "__main__":
    encryptor = FileEncryptor()

    # To set a password
    password = "my_secure_password"
    encryptor.set_password(password)

    # To encrypt a file
    encryptor.encrypt_file('file_encryption_decryption/example.txt')

    # To decrypt the file
    # Uncomment the line below to decrypt the example file
    # encryptor.decrypt_file('file_encryption_decryption/example.txt.enc')