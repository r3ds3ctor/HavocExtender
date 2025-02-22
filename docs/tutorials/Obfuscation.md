# Obfuscating Data for Stealthy Operations

## Description
This tutorial explains how to use the **Obfuscation** module to obfuscate data, making it harder to detect during exfiltration or storage.

## Requirements
- **Operating System**: Windows.
- **Havoc C2**: The Obfuscation module must be loaded.

## Steps
1. **Preparation**:
   - Load the **Obfuscation** module in Havoc C2.

2. **Execution**:
   - Use the command `obfuscate_string [string]` to obfuscate a string using base64 and XOR encryption.
   - Use the command `deobfuscate_string [encrypted_string] [key]` to deobfuscate a string.

3. **Verification**:
   - Verify the obfuscation and deobfuscation by checking the output.

## Example Commands
```bash
obfuscate_string "secret_data"
deobfuscate_string "obfuscated_data" "encryption_key"