import configparser
from .crypt import AESCipher
from .database import Database

def save_keys(key, tag, nonce, filename='keys.ini'):
    config = configparser.ConfigParser()
    config.add_section('Encryption_Keys')
    config['Encryption_Keys']['key'] = key
    config['Encryption_Keys']['tag'] = tag
    config['Encryption_Keys']['nonce'] = nonce

    with open(filename, 'w') as configfile:
        config.write(configfile)

def get_keys(filename='keys.ini'):
    config = configparser.ConfigParser()
    config.read(filename)

    key = config['Encryption_Keys']['key']
    tag = config['Encryption_Keys']['tag']
    nonce = config['Encryption_Keys']['nonce']

    return key, tag, nonce

def save_database(database, key, tag=None, nonce=None, filename='passkeysaver.dpska'):
    cipher = AESCipher(key=key)
    encrypted_database, encrypted_tag, encrypted_nonce = cipher.encrypt(database, tag=tag, nonce=nonce)

    with open(filename, 'wb') as f:
        [f.write(x) for x in (encrypted_database, encrypted_tag, encrypted_nonce)]

    return encrypted_tag, encrypted_nonce

def get_database(filename, key, tag, nonce):
    cipher = AESCipher(key=key)

    with open(filename, 'rb') as f:
        encrypted_database, encrypted_tag, encrypted_nonce = [f.read(x) for x in (16, 16, 16)]

    return cipher.decrypt(encrypted_database, encrypted_tag, encrypted_nonce)