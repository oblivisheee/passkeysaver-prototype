from Crypto.Cipher import AES
from .generator import generate_private_key_rsa
class AESCipher:
    def __init__(self, key, mode=AES.MODE_GCM):
        self.key = key
        self.mode = mode

    def encrypt(self, plaintext, tag=None, nonce=None):
        if isinstance(plaintext, str):
            plaintext = plaintext.encode('utf-8')
        cipher = AES.new(self.key, self.mode, nonce=nonce or self.nonce)
        if tag is not None:
            cipher.update(tag)
        ciphertext = cipher.encrypt(plaintext)
        return ciphertext, cipher.digest(), cipher.nonce

    def decrypt(self, ciphertext, tag, nonce):
        cipher = AES.new(self.key, self.mode, nonce=nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        return plaintext.decode('utf-8')

def generate_key(size):
    return generate_private_key_rsa(key_size=size)