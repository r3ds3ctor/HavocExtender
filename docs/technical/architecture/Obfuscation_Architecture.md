# Obfuscation Module Architecture

## Overview
The Obfuscation module obfuscates data to avoid detection during exfiltration or storage.

## Components
- **Base64 Encoding**: Encodes data using Base64.
- **XOR Encryption**: Encrypts data using XOR.

## Workflow
1. The module encodes the data using Base64.
2. It encrypts the data using XOR.
3. It decrypts and decodes the data when needed.

## Dependencies
- **Python**: The module is written in Python.
- **base64**: Used for Base64 encoding.
- **Crypto**: Used for XOR encryption.

## Limitations
- XOR encryption is not as secure as AES or RSA.
- Requires secure key management.