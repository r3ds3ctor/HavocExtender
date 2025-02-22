
---

#### **Tutorial 3: Using Privilege Escalation Tools**

**File**: `Tutorial3_Use_Tools.md`

```markdown
# Using Mimikatz for Privilege Escalation

## Description
This tutorial explains how to use **Mimikatz** to escalate privileges on a Windows system.

## Requirements
- **Operating System**: Windows.
- **Mimikatz Binary**: `mimikatz.exe` (placed in the `tools` folder).
- **Havoc C2**: The Privilege Escalation module must be loaded.

## Steps
1. **Preparation**:
   - Ensure the `mimikatz.exe` binary is available in the `tools` folder.
   - Load the **Privilege Escalation** module in Havoc C2.

2. **Execution**:
   - Use the command `use_privilege_escalation_tool Mimikatz` in the Havoc console.
   - Mimikatz will attempt to elevate the privileges of the current user.

3. **Verification**:
   - Verify the current privileges using the command `whoami /priv`.

## Example Command
```bash
use_privilege_escalation_tool Mimikatz