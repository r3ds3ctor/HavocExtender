
---

**File**: `SMB_Exec_API.md`

```markdown
# SMB Exec Module API Documentation

## Functions
### `smb_exec(target_ip, username, password, command)`
- **Description**: Executes a command on a remote system using SMB.
- **Parameters**:
  - `target_ip`: The IP address of the target system.
  - `username`: The username for authentication.
  - `password`: The password for authentication.
  - `command`: The command to execute.
- **Returns**: A string indicating success or failure.

## Example Usage
```python
from smb_exec import smb_exec

# Execute a command on a remote system
result = smb_exec("192.168.1.10", "Administrator", "P@ssw0rd", "whoami")
print(result)