
---

#### **3. Registry Persistence**

**File**: `Registry_Persistence.md`

# Creating Registry Persistence

## Description
This tutorial explains how to use the **Registry Persistence** module to create persistence on a compromised Windows system.

## Requirements
- **Operating System**: Windows.
- **Havoc C2**: The Registry Persistence module must be loaded.

## Steps
1. **Preparation**:
   - Load the **Registry Persistence** module in Havoc C2.

2. **Execution**:
   - Use the command `create_persistence [key_path] [value_name] [executable_path]` to create a registry entry for persistence.

3. **Verification**:
   - Verify the registry entry using the `regedit` tool or the `check_persistence` command.

## Example Command
```bash
create_persistence "Software\\Microsoft\\Windows\\CurrentVersion\\Run" "Backdoor" "C:\\malware.exe"