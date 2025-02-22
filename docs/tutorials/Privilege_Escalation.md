
---

#### **13. Privilege Escalation**

**File**: `Privilege_Escalation.md`

# Escalating Privileges on a Compromised System

## Description
This tutorial explains how to use the **Privilege Escalation** module to escalate privileges on a compromised system.

## Requirements
- **Operating System**: Windows.
- **Havoc C2**: The Privilege Escalation module must be loaded.

## Steps
1. **Preparation**:
   - Load the **Privilege Escalation** module in Havoc C2.

2. **Execution**:
   - Use the command `exploit_vulnerability [vulnerability]` to exploit a vulnerability for privilege escalation.
   - Use the command `abuse_misconfigurations` to abuse misconfigurations for privilege escalation.
   - Use the command `use_privilege_escalation_tool [tool_name]` to use a privilege escalation tool.

3. **Verification**:
   - Verify the escalated privileges by checking the output or using the `whoami /priv` command.

## Example Commands
```bash
exploit_vulnerability PrintNightmare
abuse_misconfigurations
use_privilege_escalation_tool Mimikatz