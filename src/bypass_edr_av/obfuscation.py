from havoc import Demon, RegisterCommand, Plugin
import base64
import random
import string

def xor_encrypt_decrypt(data, key):
    """
    Encrypts or decrypts data using XOR with a given key.
    """
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

def obfuscate_string(s):
    """
    Obfuscates a string by encoding it in base64 and applying XOR encryption.
    """
    key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8)).encode()
    encoded_str = base64.b64encode(s.encode()).decode()
    encrypted_str = xor_encrypt_decrypt(encoded_str.encode(), key)
    return encrypted_str, key

def deobfuscate_string(encrypted_str, key):
    """
    Deobfuscates a string by reversing the XOR encryption and base64 encoding.
    """
    decrypted_str = xor_encrypt_decrypt(encrypted_str, key)
    decoded_str = base64.b64decode(decrypted_str).decode()
    return decoded_str

# Havoc C2 Integration
def obfuscate_command(demon, *args):
    """
    Command to obfuscate a string.
    """
    if len(args) != 1:
        demon.ConsoleWrite("[-] Usage: obfuscate [string]")
        return

    s = args[0]
    encrypted_str, key = obfuscate_string(s)
    demon.ConsoleWrite(f"[+] Obfuscated string: {encrypted_str}")
    demon.ConsoleWrite(f"[+] Key: {key}")

def deobfuscate_command(demon, *args):
    """
    Command to deobfuscate a string.
    """
    if len(args) != 2:
        demon.ConsoleWrite("[-] Usage: deobfuscate [encrypted_string] [key]")
        return

    encrypted_str = args[0]
    key = args[1].encode()
    try:
        decrypted_str = deobfuscate_string(encrypted_str.encode(), key)
        demon.ConsoleWrite(f"[+] Deobfuscated string: {decrypted_str}")
    except Exception as e:
        demon.ConsoleWrite(f"[-] Error deobfuscating string: {e}")

# Register commands with Havoc C2
def initialize():
    RegisterCommand("obfuscate", "Obfuscate a string", obfuscate_command)
    RegisterCommand("deobfuscate", "Deobfuscate a string", deobfuscate_command)

# Initialize the plugin
plugin = Plugin("Obfuscation", "Advanced obfuscation techniques", initialize)