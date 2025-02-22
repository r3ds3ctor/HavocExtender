
---

**File**: `Credential_Dump_API.md`

```markdown
# Credential Dump Module API Documentation

## Functions
### `dump_sam_hashes()`
- **Description**: Dumps password hashes from the SAM database.
- **Returns**: A string indicating success or failure.

### `dump_lsass_memory()`
- **Description**: Dumps credentials from LSASS memory.
- **Returns**: A string indicating success or failure.

### `dump_browser_credentials()`
- **Description**: Dumps saved credentials from web browsers.
- **Returns**: A string indicating success or failure.

## Example Usage
```python
from credential_dump import dump_sam_hashes, dump_lsass_memory, dump_browser_credentials

# Dump SAM hashes
result = dump_sam_hashes()
print(result)

# Dump LSASS memory
result = dump_lsass_memory()
print(result)

# Dump browser credentials
result = dump_browser_credentials()
print(result)