
---

#### **4. WMI Persistence**

**File**: `WMI_Persistence.md`

# Creating WMI Event Subscriptions for Persistence

## Description
This tutorial explains how to use the **WMI Persistence** module to create persistence using WMI event subscriptions.

## Requirements
- **Operating System**: Windows.
- **Havoc C2**: The WMI Persistence module must be loaded.

## Steps
1. **Preparation**:
   - Load the **WMI Persistence** module in Havoc C2.

2. **Execution**:
   - Use the command `create_wmi_persistence [event_name] [executable_path] [trigger]` to create a WMI event subscription.

3. **Verification**:
   - Verify the WMI event subscription using the `check_wmi_persistence` command.

## Example Command
```bash
create_wmi_persistence "MaliciousEvent" "C:\\malware.exe" "startup"