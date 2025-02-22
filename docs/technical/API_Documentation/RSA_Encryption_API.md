
---

**File**: `RSA_Encryption_API.md`

```markdown
# RSA Encryption Module API Documentation

## Functions
### `generate_rsa_keys(key_size)`
- **Description**: Generates a pair of RSA keys (public and private).
- **Parameters**:
  - `key_size`: The size of the keys in bits.
- **Returns**: A tuple containing the private and public keys.

### `encrypt_data(data, public_key)`
- **Description**: Encrypts data using the public key.
- **Parameters**:
  - `data`: The data to encrypt.
  - `public_key`: The public key.
- **Returns**: The encrypted data.

### `decrypt_data(encrypted_data, private_key)`
- **Description**: Decrypts data using the private key.
- **Parameters**:
  - `encrypted_data`: The encrypted data.
  - `private_key`: The private key.
- **Returns**: The decrypted data.

## Example Usage
```python
from rsa_encryption import generate_rsa_keys, encrypt_data, decrypt_data

# Generate RSA keys
private_key, public_key = generate_rsa_keys(2048)

# Encrypt data
encrypted_data = encrypt_data("secret_message", public_key)
print(encrypted_data)

# Decrypt data
decrypted_data = decrypt_data(encrypted_data, private_key)
print(decrypted_data)