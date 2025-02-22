# Pass the Hash Module Architecture

## Overview
The Pass the Hash module allows authenticating to remote systems using NTLM hashes instead of plaintext passwords.

## Components
- **Hash Extraction**: Extracts NTLM hashes from the system.
- **Authentication**: Uses the hashes to authenticate to remote systems.

## Workflow
1. The module extracts NTLM hashes from the system.
2. It uses the hashes to authenticate to a remote system.
3. It executes commands on the remote system.

## Dependencies
- **Python**: The module is written in Python.
- **Impacket**: Used for Pass the Hash attacks.

## Limitations
- Only works on Windows systems.
- Requires administrative privileges for some operations.