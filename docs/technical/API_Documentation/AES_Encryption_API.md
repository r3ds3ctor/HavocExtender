
---

**File**: `AES_Encryption_API.md`

```markdown
# AES Encryption Module API Documentation

## Functions
### `encrypt_data(data, key)`
- **Description**: Encrypts data using AES.
- **Parameters**:
  - `data`: The data to encrypt.
  - `key`: The encryption key.
- **Returns**: The encrypted data.

### `decrypt_data(encrypted_data, key)`
- **Description**: Decrypts data using AES.
- **Parameters**:
  - `encrypted_data`: The encrypted data.
  - `key`: The encryption key.
- **Returns**: The decrypted data.

## Example Usage
```python
from aes_encryption import encrypt_data, decrypt_data

# Encrypt data
encrypted_data = encrypt_data("secret_message", "encryption_key")
print(encrypted_data)

# Decrypt data
decrypted_data = decrypt_data(encrypted_data, "encryption_key")
print(decrypted_data)