
---

**File**: `Process_Injection_API.md`

```markdown
# Process Injection Module API Documentation

## Functions
### `inject_shellcode(pid, shellcode)`
- **Description**: Injects shellcode into a remote process.
- **Parameters**:
  - `pid`: The process ID of the target process.
  - `shellcode`: The shellcode to inject.
- **Returns**: A string indicating success or failure.

## Example Usage
```python
from process_injection import inject_shellcode

# Inject shellcode into a remote process
result = inject_shellcode(1234, b"\x90\x90\x90")
print(result)