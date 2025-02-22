# Bypassing EDR/AV for Stealthy Execution

## Description
This tutorial explains how to use the **Bypass EDR/AV** module to evade detection by Endpoint Detection and Response (EDR) and Antivirus (AV) solutions.

## Requirements
- **Operating System**: Windows.
- **Havoc C2**: The Bypass EDR/AV module must be loaded.

## Steps
1. **Preparation**:
   - Load the **Bypass EDR/AV** module in Havoc C2.

2. **Execution**:
   - Use the command `bypass_amsi` to disable AMSI (Antimalware Scan Interface).
   - Use the command `inject_dll [pid] [dll_path]` to perform reflective DLL injection.

3. **Verification**:
   - Verify that the AMSI bypass was successful by running a script that would normally trigger AMSI.
   - Check the target process to confirm DLL injection.

## Example Commands
```bash
bypass_amsi
inject_dll 1234 malicious.dll