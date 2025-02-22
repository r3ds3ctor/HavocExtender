
---

#### **2. Process Injection**

**File**: `Process_Injection.md`

# Injecting Shellcode into Remote Processes

## Description
This tutorial explains how to use the **Process Injection** module to inject shellcode into a remote process.

## Requirements
- **Operating System**: Windows.
- **Havoc C2**: The Process Injection module must be loaded.

## Steps
1. **Preparation**:
   - Load the **Process Injection** module in Havoc C2.

2. **Execution**:
   - Use the command `inject_shellcode [pid] [shellcode_file]` to inject shellcode into a remote process.

3. **Verification**:
   - Verify that the shellcode executed successfully by checking the target process behavior.

## Example Command
```bash
inject_shellcode 1234 shellcode.bin