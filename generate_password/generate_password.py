import password_generator

if __name__ == "__main__":
    try:
        # Generate a random password with default settings
        default_password = password_generator.generate_password()
        print("Default Password:", default_password)

        # Generate a random password with custom length and included characters
        # to exclude characters use the parameter exclude_chars
        custom_password = password_generator.generate_password(length=12, include_chars='Aa1@')
        print("Custom Password:", custom_password)

        # Generate multiple passwords at once
        # to exclude characters use the parameter exclude_chars
        batch_passwords = password_generator.generate_batch_passwords(5, length=10, include_chars='Aa1@')
        print("Batch Passwords:", batch_passwords)

    except ValueError as e:
        print("Error:", str(e))
