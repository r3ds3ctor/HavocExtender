
---

**File**: `Registry_Persistence_API.md`

```markdown
# Registry Persistence Module API Documentation

## Functions
### `create_persistence(key_path, value_name, executable_path)`
- **Description**: Creates a persistence entry in the Windows Registry.
- **Parameters**:
  - `key_path`: The registry key path.
  - `value_name`: The name of the registry value.
  - `executable_path`: The path to the executable.
- **Returns**: A string indicating success or failure.

## Example Usage
```python
from registry_persistence import create_persistence

# Create a persistence entry
result = create_persistence("Software\\Microsoft\\Windows\\CurrentVersion\\Run", "Backdoor", "C:\\malware.exe")
print(result)