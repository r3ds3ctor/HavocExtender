# Process Injection Module Architecture

## Overview
The Process Injection module allows injecting shellcode into a remote process, enabling execution of malicious code in the context of another process.

## Components
- **Shellcode Injection**: Injects shellcode into a target process.
- **Memory Allocation**: Allocates memory in the target process for the shellcode.

## Workflow
1. The module opens the target process.
2. It allocates memory in the target process.
3. It writes the shellcode into the allocated memory.
4. It creates a remote thread to execute the shellcode.

## Dependencies
- **Python**: The module is written in Python.
- **ctypes**: Used to interact with the Windows API.

## Limitations
- Only works on Windows systems.
- Requires administrative privileges for some operations.