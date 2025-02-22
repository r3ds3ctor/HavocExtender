
---

#### **Tutorial 2: Abusing Misconfigurations for Privilege Escalation**

**File**: `Tutorial2_Abuse_Misconfigurations.md`

```markdown
# Abusing Misconfigurations for Privilege Escalation

## Description
This tutorial explains how to abuse misconfigured services to escalate privileges on a Windows system.

## Requirements
- **Operating System**: Windows.
- **Havoc C2**: The Privilege Escalation module must be loaded.

## Steps
1. **Preparation**:
   - Load the **Privilege Escalation** module in Havoc C2.

2. **Execution**:
   - Use the command `abuse_misconfigurations` in the Havoc console.
   - The module will search for weakly configured services and attempt to start them.

3. **Verification**:
   - Verify the started services using the command `Get-Service`.

## Example Command
```bash
abuse_misconfigurations