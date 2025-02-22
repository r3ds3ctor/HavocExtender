
---

#### **5. Scheduled Task**

**File**: `Scheduled_Task.md`

# Creating Scheduled Tasks for Persistence

## Description
This tutorial explains how to use the **Scheduled Task** module to create persistence using scheduled tasks.

## Requirements
- **Operating System**: Windows.
- **Havoc C2**: The Scheduled Task module must be loaded.

## Steps
1. **Preparation**:
   - Load the **Scheduled Task** module in Havoc C2.

2. **Execution**:
   - Use the command `create_scheduled_task [task_name] [executable_path] [trigger]` to create a scheduled task.

3. **Verification**:
   - Verify the scheduled task using the `schtasks` command or the `check_scheduled_task` command.

## Example Command
```bash
create_scheduled_task "MaliciousTask" "C:\\malware.exe" "startup"