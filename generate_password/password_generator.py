import string
import random

def generate_password(length=12, include_chars=None, exclude_chars=None):
    # Define all possible characters
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Determine the valid characters based on user input
    if include_chars:
        valid_chars = include_chars  # Use user-specified characters if provided
    else:
        if exclude_chars:
            valid_chars = ''.join(set(all_chars) - set(exclude_chars))
        else:
            valid_chars = all_chars  # Use all characters by default

    # Check if the valid character set is empty
    if not valid_chars:
        raise ValueError("Invalid character set. Make sure to include or exclude valid characters.")

    # Generate the password by randomly choosing characters
    password = ''.join(random.choice(valid_chars) for i in range(length))
    return password

def generate_batch_passwords(num_passwords, length=12, include_chars=None, exclude_chars=None):
    passwords = []
    for i in range(num_passwords):
        password = generate_password(length, include_chars, exclude_chars)
        passwords.append(password)
    return passwords
