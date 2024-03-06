import art
from .database import Database
import save
from .generator import generate_private_key_rsa, generate_password
import os
import sys

class PassKeySaver:
    def __init__(self):
        self.settings = []
        self.available_choices = [1, 2, 3, 4, 5, 6]
        self.database = Database()
        self._first_started = False
        self.private_key = None

    def run(self):
        if not self._first_started:
            self._first_start()
        self.main_interface()

    def _first_start(self):
        self._first_started = True
        print(self._logo("Welcome!"))
        print("Do you want to import a key or generate a new one?\n1. Import key\n2. Generate key")
        choice = int(input("Enter the number of your choice: "))
        if choice == 2:
            print("Generating your key...")
            self.private_key = generate_private_key_rsa()
            print("Key generation successful")
        elif choice == 1:
            key = input("Enter your private key: ")
            self.private_key = key
        else:
            print("Invalid choice")
            self._first_start()

    def main_interface(self):
        print(self._logo("PassKeySaver"))
        while True:
            self._display_options()
            try:
                option = int(input("Choose an option: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if option in self.available_choices:
                self._handle_option(option)
            else:
                print("Invalid option. Please try again.")

    def _display_options(self):
        print("\n1. Add new password")
        print("2. Show all passwords")
        print("3. Edit a password")
        print("4. Delete a password")
        print("5. Exit PassKeySaver")
        print("6. Generate password")

    def _handle_option(self, option):
        if option == 1:
            self.add_password()
        elif option == 2:
            self.show_passwords()
        elif option == 3:
            self.edit_password()
        elif option == 4:
            self.delete_password()
        elif option == 5:
            print("Exiting...")
            if self._first_started:
                tag, nonce = save.save_database(self.database, self.private_key)
                save.save_keys(self.private_key, tag, nonce)
            else:
                save.save_keys(self.database)
            sys.exit()
        elif option == 5:
            length = int(input("Enter password length: "))
            use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
            use_special = input("Include special characters? (y/n): ").lower() == 'y'
            use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
            password = generate_password(length=length, use_upper=use_upper, use_numbers=use_numbers, use_symbols=use_special)
            print(password)
        else:
            print("Invalid option. Please try again.")

    def _logo(self, name):
        return art.text2art(name)

    def add_password(self):
        name = input("Enter password name: ")
        login = input("Enter login: ")
        password = input("Enter password: ")
        other = input("Enter other info: ")
        self.database.add_pass(name, login, password, other)

    def show_passwords(self):
        print(self.database.show_all_passes())
        input("Press any key to return...")

    def edit_password(self):
        pass  # Implement this method

    def delete_password(self):
        pass  # Implement this method


if __name__ == "__main__":
    app = PassKeySaver()
    app.run()