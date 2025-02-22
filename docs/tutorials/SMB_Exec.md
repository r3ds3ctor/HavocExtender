
---

#### **7. SMB Exec**

**File**: `SMB_Exec.md`

# Executing Commands via SMB

## Description
This tutorial explains how to use the **SMB Exec** module to execute commands on remote systems using the SMB protocol.

## Requirements
- **Operating System**: Windows.
- **Havoc C2**: The SMB Exec module must be loaded.

## Steps
1. **Preparation**:
   - Load the **SMB Exec** module in Havoc C2.

2. **Execution**:
   - Use the command `smb_exec [target_ip] [username] [password] [command]` to execute a command on a remote system.

3. **Verification**:
   - Verify the command execution by checking the output or the remote system.

## Example Command
```bash
smb_exec 192.168.1.10 Administrator P@ssw0rd "whoami"