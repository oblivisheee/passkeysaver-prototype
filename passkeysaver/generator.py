import random
import string
from Crypto.PublicKey import RSA
def generate_password(length=8, use_upper=True, use_numbers=True, use_symbols=True):
    all_characters = string.ascii_lowercase
    if use_upper:
        all_characters += string.ascii_uppercase
    if use_numbers:
        all_characters += string.digits
    if use_symbols:
        all_characters += string.punctuation

    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def generate_private_key_rsa(key_size=2048) -> str:
    key = RSA.generate(key_size)
    private_key = key.export_key().decode('utf-8')
    return private_key + '\n'