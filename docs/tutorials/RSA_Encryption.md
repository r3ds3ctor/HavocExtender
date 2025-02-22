
---

#### **11. RSA Encryption**

**File**: `RSA_Encryption.md`

# Encrypting Data Using RSA

## Description
This tutorial explains how to use the **RSA Encryption** module to encrypt and decrypt data using the RSA algorithm.

## Requirements
- **Operating System**: Windows.
- **Havoc C2**: The RSA Encryption module must be loaded.

## Steps
1. **Preparation**:
   - Load the **RSA Encryption** module in Havoc C2.

2. **Execution**:
   - Use the command `generate_rsa_keys` to generate a pair of RSA keys.
   - Use the command `encrypt_data [public_key] [data]` to encrypt data.
   - Use the command `decrypt_data [private_key] [encrypted_data]` to decrypt data.

3. **Verification**:
   - Verify the encryption and decryption by checking the output.

## Example Commands
```bash
generate_rsa_keys
encrypt_data "public_key" "secret_message"
decrypt_data "private_key" "encrypted_data"