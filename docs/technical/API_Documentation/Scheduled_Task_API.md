
---

**File**: `Scheduled_Task_API.md`

```markdown
# Scheduled Task Module API Documentation

## Functions
### `create_scheduled_task(task_name, executable_path, trigger)`
- **Description**: Creates a scheduled task for persistence.
- **Parameters**:
  - `task_name`: The name of the task.
  - `executable_path`: The path to the executable.
  - `trigger`: The trigger for the task (e.g., "startup").
- **Returns**: A string indicating success or failure.

## Example Usage
```python
from scheduled_task import create_scheduled_task

# Create a scheduled task
result = create_scheduled_task("MaliciousTask", "C:\\malware.exe", "startup")
print(result)