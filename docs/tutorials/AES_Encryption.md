
---

#### **10. AES Encryption**

**File**: `AES_Encryption.md`

# Encrypting Data Using AES

## Description
This tutorial explains how to use the **AES Encryption** module to encrypt and decrypt data using the AES algorithm.

## Requirements
- **Operating System**: Windows.
- **Havoc C2**: The AES Encryption module must be loaded.

## Steps
1. **Preparation**:
   - Load the **AES Encryption** module in Havoc C2.

2. **Execution**:
   - Use the command `encrypt_data [data]` to encrypt data.
   - Use the command `decrypt_data [encrypted_data]` to decrypt data.

3. **Verification**:
   - Verify the encryption and decryption by checking the output.

## Example Commands
```bash
encrypt_data "secret_message"
decrypt_data "encrypted_data"