from havoc import Demon, RegisterCommand, Plugin
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def generate_rsa_keys(key_size=2048):
    """
    Generates a pair of RSA keys (public and private).
    """
    try:
        key = RSA.generate(key_size)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        return private_key, public_key
    except Exception as e:
        return f"[-] Error generating RSA keys: {e}"

def encrypt_data(data, public_key):
    """
    Encrypts data using RSA public key.
    """
    try:
        rsa_key = RSA.import_key(public_key)
        cipher = PKCS1_OAEP.new(rsa_key)
        encrypted_data = cipher.encrypt(data.encode())
        return base64.b64encode(encrypted_data).decode()
    except Exception as e:
        return f"[-] Error encrypting data: {e}"

def decrypt_data(encrypted_data, private_key):
    """
    Decrypts data using RSA private key.
    """
    try:
        encrypted_data = base64.b64decode(encrypted_data)
        rsa_key = RSA.import_key(private_key)
        cipher = PKCS1_OAEP.new(rsa_key)
        decrypted_data = cipher.decrypt(encrypted_data)
        return decrypted_data.decode()
    except Exception as e:
        return f"[-] Error decrypting data: {e}"

# Havoc C2 Integration
def generate_keys_command(demon, *args):
    """
    Command to generate RSA keys.
    """
    key_size = 2048  # Default key size
    if len(args) == 1:
        try:
            key_size = int(args[0])
        except ValueError:
            demon.ConsoleWrite("[-] Invalid key size. Using default (2048).")
            key_size = 2048

    private_key, public_key = generate_rsa_keys(key_size)
    demon.ConsoleWrite(f"[+] Private Key:\n{private_key.decode()}")
    demon.ConsoleWrite(f"[+] Public Key:\n{public_key.decode()}")

def encrypt_data_command(demon, *args):
    """
    Command to encrypt data using RSA public key.
    """
    if len(args) != 2:
        demon.ConsoleWrite("[-] Usage: encrypt_data [public_key] [data]")
        return

    public_key = args[0]
    data = args[1]

    result = encrypt_data(data, public_key)
    demon.ConsoleWrite(f"[+] Encrypted data: {result}")

def decrypt_data_command(demon, *args):
    """
    Command to decrypt data using RSA private key.
    """
    if len(args) != 2:
        demon.ConsoleWrite("[-] Usage: decrypt_data [private_key] [encrypted_data]")
        return

    private_key = args[0]
    encrypted_data = args[1]

    result = decrypt_data(encrypted_data, private_key)
    demon.ConsoleWrite(f"[+] Decrypted data: {result}")

# Register commands with Havoc C2
def initialize():
    RegisterCommand("generate_rsa_keys", "Generate RSA public and private keys", generate_keys_command)
    RegisterCommand("encrypt_data", "Encrypt data using RSA public key", encrypt_data_command)
    RegisterCommand("decrypt_data", "Decrypt data using RSA private key", decrypt_data_command)

# Initialize the plugin
plugin = Plugin("RSAEncryption", "Advanced RSA encryption techniques", initialize)