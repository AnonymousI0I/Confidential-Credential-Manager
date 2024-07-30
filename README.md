# Confidential Credential Manager

This Python script provides a comprehensive solution for managing and encrypting passwords securely. The main functionalities include:

1. Generating and saving encryption keys.
2. Encrypting and decrypting passwords.
3. Saving and retrieving encrypted passwords.
4. Generating random secure passwords.
5. Resetting the app to set a new parent password.

## Features

- **Encrypt and Decrypt Passwords**: Secure your passwords using encryption.
- **Save and Retrieve Passwords**: Store and access encrypted passwords.
- **Generate Random Passwords**: Create strong, random passwords.
- **Reset App**: Reset the application to set a new parent password and delete all stored data.

## Requirements

- Python 3.x
- `cryptography` module

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/confidential-credential-manager.git
    cd confidential-credential-manager
    ```

2. **Install the required module**:

    ```bash
    pip install cryptography
    ```

3. **Ensure Python 3.x is installed on your machine**.

## Usage

1. **Run the script**:

    ```bash
    python password_manager.py
    ```

2. **Follow the on-screen prompts to add, retrieve, list usernames, reset the app, or quit**:

### Adding a Password

- You will be prompted to enter the account name and password.
- If you leave the password blank, a random password will be generated.

    Example:

    ```
    Do you want to add a new password, retrieve a password, list usernames, or quit? (add/retrieve/list/quit): add
    Enter the account name: GitHub
    Enter the password (leave blank to generate a random password):
    Generated password: A1b2C3d4E5!
    Password for GitHub saved.
    ```

### Retrieving a Password

- You will be prompted to enter the account name to retrieve the password.

    Example:

    ```
    Do you want to add a new password, retrieve a password, list usernames, or quit? (add/retrieve/list/quit): retrieve
    Enter the account name: GitHub
    The password for GitHub is A1b2C3d4E5!
    ```

### Listing Usernames

- You will be prompted to list all saved usernames.

    Example:

    ```
    Do you want to add a new password, retrieve a password, list usernames, or quit? (add/retrieve/list/quit): list
    Saved usernames:
    GitHub
    ```

### Resetting the App

- You will be prompted to confirm the reset. This will delete all stored usernames and passwords and allow you to set a new parent password.

    Example:

    ```
    Enter the parent password or type 'reset' to reset the app: reset
    Are you sure you want to reset the app? This will delete all stored usernames and passwords. Type 'yes' to confirm: yes
    App reset successfully. Please restart the program to set a new parent password.
    ```

### Quitting the Program

- Enter `quit` to exit the password manager.

    Example:

    ```
    Do you want to add a new password, retrieve a password, list usernames, or quit? (add/retrieve/list/quit): quit
    Exiting the password manager.
    ```

## Code Overview

### Function Descriptions

#### `generate_key()`

Generates an encryption key and saves it to a file.

#### `load_key()`

Loads the encryption key from a file.

#### `encrypt_password(password, key)`

Encrypts the given password using the provided key.

- **Parameters**:
  - `password` (str): The password to encrypt.
  - `key` (bytes): The encryption key.
- **Returns**:
  - `bytes`: The encrypted password.

#### `decrypt_password(encrypted_password, key)`

Decrypts the given encrypted password using the provided key.

- **Parameters**:
  - `encrypted_password` (bytes): The encrypted password.
  - `key` (bytes): The encryption key.
- **Returns**:
  - `str`: The decrypted password.

#### `save_parent_password(password)`

Saves the parent password using encryption.

- **Parameters**:
  - `password` (str): The parent password.

#### `load_parent_password()`

Loads and decrypts the parent password.

- **Returns**:
  - `str`: The decrypted parent password.

#### `initial_prompt()`

Prompts the user to enter the parent password or reset the app.

#### `save_password(account, password)`

Saves the encrypted password for the specified account.

- **Parameters**:
  - `account` (str): The account name.
  - `password` (str): The password to save.

#### `retrieve_password(account)`

Retrieves the decrypted password for the specified account.

- **Parameters**:
  - `account` (str): The account name.
- **Returns**:
  - `str`: The decrypted password, or `None` if the account is not found.

#### `generate_password(length=12)`

Generates a random secure password of the specified length.

- **Parameters**:
  - `length` (int): The length of the password. Default is 12.
- **Returns**:
  - `str`: The generated password.

#### `list_usernames()`

Lists all saved usernames.

- **Returns**:
  - `list`: A list of saved usernames.

#### `reset_app()`

Resets the app, deleting all stored usernames and passwords and allowing the user to set a new parent password.

#### `main()`

Handles user input and orchestrates the workflow of the program.

- Prompts the user to add, retrieve, list, or quit.
- Saves and retrieves passwords using encryption.

## Contribution

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request.
