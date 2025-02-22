# Bypass EDR/AV Module Architecture

## Overview
The Bypass EDR/AV module is designed to evade detection by Endpoint Detection and Response (EDR) and Antivirus (AV) solutions. It achieves this by using techniques such as AMSI bypass and reflective DLL injection.

## Components
- **AMSI Bypass**: Disables the Antimalware Scan Interface (AMSI) to avoid script detection.
- **Reflective DLL Injection**: Injects a DLL into a remote process without touching the disk.

## Workflow
1. The module checks if the system is Windows.
2. It disables AMSI by patching the `amsi.dll` in memory.
3. It injects a DLL into a target process using reflective DLL injection.

## Dependencies
- **Python**: The module is written in Python.
- **ctypes**: Used to interact with the Windows API.
- **pywin32**: Provides access to Windows-specific functionality.

## Limitations
- Only works on Windows systems.
- Requires administrative privileges for some operations.