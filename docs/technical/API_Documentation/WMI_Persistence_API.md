
---

**File**: `WMI_Persistence_API.md`

```markdown
# WMI Persistence Module API Documentation

## Functions
### `create_wmi_persistence(event_name, executable_path, trigger)`
- **Description**: Creates a WMI event subscription for persistence.
- **Parameters**:
  - `event_name`: The name of the event.
  - `executable_path`: The path to the executable.
  - `trigger`: The trigger for the event (e.g., "startup").
- **Returns**: A string indicating success or failure.

## Example Usage
```python
from wmi_persistence import create_wmi_persistence

# Create a WMI event subscription
result = create_wmi_persistence("MaliciousEvent", "C:\\malware.exe", "startup")
print(result)