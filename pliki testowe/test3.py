import hashlib
import os

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Generowanie klucza RSA
private_key = rsa.generate_private_key(public_exponent=65536, key_size=1024, backend=default_backend())

# Generowanie klucza AES
secret_key = hashlib.md5(b"my_secret_key").digest()


# Szyfrowanie danych AES
def encrypt_data(data, key):
    iv = os.urandom(16)
    encryptor = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend()).encryptor()
    ciphertext = encryptor.update(data) + encryptor.finalize()
    return iv, ciphertext


# Deszyfrowanie danych AES
def decrypt_data(encrypted_data, key, iv):
    decryptor = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend()).decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    return decrypted_data


# Podpis cyfrowy danych za pomocą klucza RSA
def sign_data(data, private_key):
    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature


# Weryfikacja podpisu cyfrowego danych za pomocą klucza publicznego RSA
def verify_signature(data, signature, public_key):
    try:
        public_key.verify(
            signature,
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False


# Przykładowe użycie funkcji

data_to_encrypt = b"Sensitive information"
iv, encrypted_data = encrypt_data(data_to_encrypt, secret_key)
signature = sign_data(data_to_encrypt, private_key)
verification_result = verify_signature(data_to_encrypt, signature, private_key.public_key())

print("Encryption and signature verification result:", verification_result)
