
---

#### **6. Pass the Hash**

**File**: `Pass_the_Hash.md`

# Performing Pass the Hash Attacks

## Description
This tutorial explains how to use the **Pass the Hash** module to authenticate to remote systems using NTLM hashes.

## Requirements
- **Operating System**: Windows.
- **Havoc C2**: The Pass the Hash module must be loaded.

## Steps
1. **Preparation**:
   - Load the **Pass the Hash** module in Havoc C2.

2. **Execution**:
   - Use the command `pass_the_hash [target_ip] [username] [ntlm_hash] [command]` to execute a command on a remote system.

3. **Verification**:
   - Verify the command execution by checking the output or the remote system.

## Example Command
```bash
pass_the_hash 192.168.1.10 Administrator aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0 "whoami"