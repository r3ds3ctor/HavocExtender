# Registry Persistence Module Architecture

## Overview
The Registry Persistence module creates persistence on a compromised system by adding entries to the Windows Registry.

## Components
- **Registry Key Creation**: Adds a new key to the registry.
- **Value Assignment**: Assigns a value to the key, pointing to a malicious executable.

## Workflow
1. The module opens the target registry key.
2. It creates a new value in the key.
3. It assigns the value to point to the malicious executable.

## Dependencies
- **Python**: The module is written in Python.
- **winreg**: Used to interact with the Windows Registry.

## Limitations
- Only works on Windows systems.
- Requires administrative privileges for some operations.