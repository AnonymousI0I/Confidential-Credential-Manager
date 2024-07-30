import os
import json
import random
import string
from cryptography.fernet import Fernet

# Function to generate a key and save it into a file
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Function to load the key from the current directory named `secret.key`
def load_key():
    return open("secret.key", "rb").read()

# Function to encrypt a password
def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# Function to decrypt a password
def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# Function to save parent password
def save_parent_password(password):
    key = load_key()
    encrypted_password = encrypt_password(password, key)
    with open("parent_password.key", "wb") as file:
        file.write(encrypted_password)

# Function to load parent password
def load_parent_password():
    key = load_key()
    with open("parent_password.key", "rb") as file:
        encrypted_password = file.read()
    return decrypt_password(encrypted_password, key)

# Function to verify parent password or reset app
def initial_prompt():
    if not os.path.exists("parent_password.key"):
        print("No parent password set. You must set a parent password to use the password manager.")
        password = input("Set a new parent password: ")
        save_parent_password(password)
        print("Parent password set. Please restart the program.")
        exit()
    else:
        while True:
            choice = input("Enter the parent password or type 'reset' to reset the app: ").strip().lower()
            if choice == "reset":
                reset_app()
            elif choice == load_parent_password():
                break
            else:
                print("Incorrect parent password. Please try again.")

# Function to save passwords
def save_password(account, password):
    key = load_key()
    encrypted_password = encrypt_password(password, key)
    
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            passwords = json.load(file)
    else:
        passwords = {}

    passwords[account] = encrypted_password.decode()

    with open("passwords.json", "w") as file:
        json.dump(passwords, file)

# Function to retrieve passwords
def retrieve_password(account):
    key = load_key()
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            passwords = json.load(file)
            if account in passwords:
                encrypted_password = passwords[account].encode()
                return decrypt_password(encrypted_password, key)
            else:
                return None
    else:
        return None

# Function to generate a random password
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Function to list all saved usernames
def list_usernames():
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            passwords = json.load(file)
            return list(passwords.keys())
    else:
        return []

# Function to reset the app
def reset_app():
    confirmation = input("Are you sure you want to reset the app? This will delete all stored usernames and passwords. Type 'yes' to confirm: ").strip().lower()
    if confirmation == 'yes':
        if os.path.exists("parent_password.key"):
            os.remove("parent_password.key")
        if os.path.exists("passwords.json"):
            os.remove("passwords.json")
        print("App reset successfully. Please restart the program to set a new parent password.")
        exit()
    else:
        print("Reset cancelled.")

def main():
    if not os.path.exists("secret.key"):
        generate_key()

    initial_prompt()

    while True:
        choice = input("Do you want to add a new password, retrieve a password, list usernames, or quit? (add/retrieve/list/quit): ").strip().lower()
        if choice == "add":
            account = input("Enter the account name: ").strip()
            password = input("Enter the password (leave blank to generate a random password): ").strip()
            if not password:
                password = generate_password()
                print(f"Generated password: {password}")
            save_password(account, password)
            print(f"Password for {account} saved.")
        elif choice == "retrieve":
            account = input("Enter the account name: ").strip()
            password = retrieve_password(account)
            if password:
                print(f"The password for {account} is {password}")
            else:
                print(f"No password found for {account}.")
        elif choice == "list":
            usernames = list_usernames()
            if usernames:
                print("Saved usernames:")
                for username in usernames:
                    print(username)
            else:
                print("No usernames found.")
        elif choice == "quit":
            print("Exiting the password manager.")
            break
        else:
            print("Invalid choice. Please choose 'add', 'retrieve', 'list', or 'quit'.")

if __name__ == "__main__":
    main()
