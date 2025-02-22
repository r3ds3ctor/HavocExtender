from havoc import Demon, RegisterCommand, Plugin  # Importamos la clase Plugin
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# AES encryption key (must be 16, 24, or 32 bytes long)
AES_KEY = b'ThisIsASecretKey'

def encrypt_data(data, key):
    """
    Encrypts data using AES encryption.
    """
    try:
        cipher = AES.new(key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(data.encode(), AES.block_size))
        return base64.b64encode(cipher.iv + ciphertext).decode()
    except Exception as e:
        return f"[-] Error encrypting data: {e}"

def decrypt_data(encrypted_data, key):
    """
    Decrypts data using AES encryption.
    """
    try:
        encrypted_data = base64.b64decode(encrypted_data)
        iv = encrypted_data[:AES.block_size]
        ciphertext = encrypted_data[AES.block_size:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return plaintext.decode()
    except Exception as e:
        return f"[-] Error decrypting data: {e}"

# Havoc C2 Integration
def encrypt_data_command(demon, *args):
    """
    Command to encrypt data using AES.
    """
    if len(args) != 1:
        demon.ConsoleWrite("[-] Usage: encrypt_data [data]")
        return

    data = args[0]

    result = encrypt_data(data, AES_KEY)
    demon.ConsoleWrite(f"[+] Encrypted data: {result}")

def decrypt_data_command(demon, *args):
    """
    Command to decrypt data using AES.
    """
    if len(args) != 1:
        demon.ConsoleWrite("[-] Usage: decrypt_data [encrypted_data]")
        return

    encrypted_data = args[0]

    result = decrypt_data(encrypted_data, AES_KEY)
    demon.ConsoleWrite(f"[+] Decrypted data: {result}")

# Register commands with Havoc C2
def initialize():
    RegisterCommand("encrypt_data", "Encrypt data using AES", encrypt_data_command)
    RegisterCommand("decrypt_data", "Decrypt data using AES", decrypt_data_command)

# Initialize the plugin
plugin = Plugin("AESEncryption", "Advanced AES encryption techniques", initialize)