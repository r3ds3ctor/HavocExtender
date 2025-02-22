
---

#### **12. Credential Dump**

**File**: `Credential_Dump.md`

# Dumping Credentials from a Compromised System

## Description
This tutorial explains how to use the **Credential Dump** module to extract credentials from a compromised system.

## Requirements
- **Operating System**: Windows.
- **Havoc C2**: The Credential Dump module must be loaded.

## Steps
1. **Preparation**:
   - Load the **Credential Dump** module in Havoc C2.

2. **Execution**:
   - Use the command `dump_sam_hashes` to dump password hashes from the SAM database.
   - Use the command `dump_lsass_memory` to dump credentials from LSASS memory.
   - Use the command `dump_browser_credentials` to dump saved credentials from web browsers.

3. **Verification**:
   - Verify the dumped credentials by checking the output.

## Example Commands
```bash
dump_sam_hashes
dump_lsass_memory
dump_browser_credentials