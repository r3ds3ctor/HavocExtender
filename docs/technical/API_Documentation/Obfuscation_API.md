
---

**File**: `Obfuscation_API.md`

```markdown
# Obfuscation Module API Documentation

## Functions
### `obfuscate_string(s)`
- **Description**: Obfuscates a string using Base64 and XOR encryption.
- **Parameters**:
  - `s`: The string to obfuscate.
- **Returns**: A tuple containing the obfuscated string and the encryption key.

### `deobfuscate_string(encrypted_str, key)`
- **Description**: Deobfuscates a string using XOR encryption and Base64 decoding.
- **Parameters**:
  - `encrypted_str`: The obfuscated string.
  - `key`: The encryption key.
- **Returns**: The original string.

## Example Usage
```python
from obfuscation import obfuscate_string, deobfuscate_string

# Obfuscate a string
encrypted_str, key = obfuscate_string("secret_data")
print(f"Obfuscated: {encrypted_str}, Key: {key}")

# Deobfuscate a string
original_str = deobfuscate_string(encrypted_str, key)
print(f"Deobfuscated: {original_str}")