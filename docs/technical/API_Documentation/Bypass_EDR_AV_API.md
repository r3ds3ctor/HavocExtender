# Bypass EDR/AV Module API Documentation

## Functions
### `bypass_amsi()`
- **Description**: Disables AMSI by patching the `amsi.dll` in memory.
- **Returns**: A string indicating success or failure.

### `inject_dll(pid, dll_path)`
- **Description**: Injects a DLL into a remote process using reflective DLL injection.
- **Parameters**:
  - `pid`: The process ID of the target process.
  - `dll_path`: The path to the DLL to inject.
- **Returns**: A string indicating success or failure.

## Example Usage
```python
from bypass_edr_av import bypass_amsi, inject_dll

# Disable AMSI
result = bypass_amsi()
print(result)

# Inject a DLL into a remote process
result = inject_dll(1234, "malicious.dll")
print(result)