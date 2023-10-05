import password_generator

# Generate a random password with default settings
default_password = password_generator.generate_password()

# Generate a random password with custom length and included characters
custom_password = password_generator.generate_password(length=12, include_chars='Aa1@')

# Generate multiple passwords at once
batch_passwords = password_generator.generate_batch_passwords(5, length=10, include_chars='Aa1@')