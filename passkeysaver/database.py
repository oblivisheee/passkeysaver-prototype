from typing import Dict, Optional
from .crypt import AESCipher

class Database:
    def __init__(self):
        self._database: Dict[str, Dict[str, str]] = {}

    def add_pass(self, name: str, login: str, password: str, other: str) -> None:
        """
        Add a new entry to the database.

        :param name: The name of the entry
        :param login: The login information
        :param password: The password information
        :param other: Other information
        """
        self._database[name] = {
            "login": login,
            "password": password,
            "other": other
        }

    def get_pass(self, name: str) -> Dict[str, str]:
        """
        Get the information for an entry by name.

        :param name: The name of the entry
        :return: The information for the given entry
        """
        return self._database.get(name, {})

    def show_all_passes(self) -> str:
        """
        Get a string representation of all entries in the database.

        :return: A string with the details of all entries
        """
        data = ''
        for name, info in self._database.items():
            data += f"{name}::{info['login']}::{info['password']}::{info['other']}\n"
        return data

    def change_pass(self, name: str, **changes: str) -> None:
        """
        Update information for an entry.

        :param name: The name of the entry
        :param changes: Keyword arguments with the information to update
            (e.g., "login"="new_login", "password"="new_password", "other"="new_other")
        """
        pass_info = self._database.get(name, {})
        for key, value in changes.items():
            if key in ("login", "password", "other"):
                pass_info[key] = value
        self._database[name] = pass_info

    def get(self) -> Dict[str, Dict[str, str]]:
        """
        Get the database as a dictionary.

        :return: The database as a dictionary
        """
        return self._database