from base64 import b64encode, b64decode
from pyDes import des, CBC, PAD_PKCS5
import os

# Generate a key for DES encryption
def generate_des_key(password):
    return password[:8].encode()

# Encrypt a message using DES
def encrypt_message(message, key):
    iv = os.urandom(8)  # Generate a random initialization vector
    cipher = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    encrypted_message = cipher.encrypt(message.encode())
    return b64encode(iv + encrypted_message).decode()

# Decrypt a message using DES
def decrypt_message(encrypted_message, key):
    encrypted_data = b64decode(encrypted_message)
    iv = encrypted_data[:8]
    ciphertext = encrypted_data[8:]
    cipher = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    decrypted_message = cipher.decrypt(ciphertext)
    return decrypted_message.decode()

# Example usage
if __name__ == "__main__":
    password = input("Enter the password you want to keep: ") # Replace this with your password
    message = input("Enter the message: ")

    # Generate DES key
    key = generate_des_key(password)

    # Encrypt the message
    encrypted_message = encrypt_message(message, key)
    print("Encrypted:", encrypted_message)

    # Decrypt the message
    decrypted_message = decrypt_message(encrypted_message, key)
    print("Decrypted:", decrypted_message)
