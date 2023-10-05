# Random Password Generator

Random Password Generator is a Python script that allows users to generate random passwords with various customizable options, including password length, character inclusion/exclusion, and more. This script helps users create secure and personalized passwords for their needs.

## Features

- **Customizable Length:** Users can specify the desired length of the generated password.
- **Character Inclusion/Exclusion:** Provides options to include or exclude specific characters or character sets (e.g., uppercase, lowercase, numbers, symbols).
- **Secure Randomization:** Implements a secure randomization algorithm to ensure password strength.
- **Generate Multiple Passwords:** Users can generate a batch of random passwords at once.

## Usage

1. Import the `password_generator` module into your Python script or program:

    ```python
    import password_generator
    ```

2. Generate a random password with default settings:

    ```python
    default_password = password_generator.generate_password()
    print("Default Password:", default_password)
    ```

3. Generate a random password with custom length and included characters:

    ```python
    custom_password = password_generator.generate_password(length=12, include_chars='Aa1@')
    print("Custom Password:", custom_password)
    ```

4. Generate multiple passwords at once:

    ```python
    batch_passwords = password_generator.generate_batch_passwords(5, length=10, include_chars='Aa1@')
    print("Batch Passwords:", batch_passwords)
    ```

5. Ensure that you handle any potential errors or exceptions, such as an invalid character set.

## Installation

There's no need for installation; you can simply include the `password_generator.py` file in your project and import the functions as shown in the usage section.


Happy password generating!
