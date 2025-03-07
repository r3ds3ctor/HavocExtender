# HavocExtender - Advanced Extensions for Havoc C2

## Project Structure
```
HavocExtender/
├── README.md  # Project description, objectives, key features, requirements, installation, and usage
├── LICENSE  # Defines the project license (e.g., MIT, GPL)
├── CONTRIBUTING.md  # Contribution guidelines (code standards, pull requests, etc.)
├── CHANGELOG.md  # Change log and updates
├── src/
│   ├── bypass_edr_av/  # Evasion techniques for EDR/AV
│   │   ├── edr_bypass.py
│   │   ├── process_injection.py
│   │   ├── obfuscation.py
│   ├── persistence/  # Advanced persistence modules
│   │   ├── registry_persistence.py
│   │   ├── wmi_persistence.py
│   │   ├── scheduled_task.py
│   ├── lateral_movement/  # Lateral movement tools
│   │   ├── pass_the_hash.py
│   │   ├── smb_exec.py
│   ├── exfiltration/  # Secure exfiltration methods
│   │   ├── file_exfil.py
│   │   ├── dns_tunnel.py
│   ├── encryption/  # Enhanced encryption implementations
│   │   ├── aes_encryption.py
│   │   ├── rsa_encryption.py
│   ├── post_exploitation/  # Post-exploitation automation scripts
│   │   ├── credential_dump.py
│   │   ├── privilege_escalation.py
├── docs/  # Detailed project documentation
│   ├── tutorials/  # Step-by-step guides for each module
│   ├── technical/  # Technical specifications and architecture
├── tests/  # Unit and integration tests for each module
│   ├── test_bypass.py
│   ├── test_persistence.py
│   ├── test_lateral_movement.py
│   ├── test_exfiltration.py
├── examples/  # Usage examples and configurations
├── scripts/  # Auxiliary scripts for compilation, deployment, or configuration
``` 

## Modules Overview

### Evasion (`bypass_edr_av/`)
- **EDR Bypass (`edr_bypass.py`)**: Restores original API hooks, evading EDR detection.
- **Process Injection (`process_injection.py`)**: Uses advanced injection techniques to stealthily execute payloads.
- **Obfuscation (`obfuscation.py`)**: Implements encryption techniques to hide execution traces.

### Persistence (`persistence/`)
- **Registry Persistence (`registry_persistence.py`)**: Adds hidden registry keys for stealthy startup execution.
- **WMI Persistence (`wmi_persistence.py`)**: Uses WMI Event Subscription for persistent access.
- **Scheduled Task (`scheduled_task.py`)**: Creates hidden scheduled tasks for persistent execution.

### Lateral Movement (`lateral_movement/`)
- **Pass-the-Hash (`pass_the_hash.py`)**: Uses NTLM hash injection for credential-less authentication.
- **SMB Execution (`smb_exec.py`)**: Executes remote commands via SMB protocol.

### Exfiltration (`exfiltration/`)
- **File Exfiltration (`file_exfil.py`)**: Secure file transfer over encrypted channels.
- **DNS Tunneling (`dns_tunnel.py`)**: Encodes and exfiltrates data via DNS queries.

### Encryption (`encryption/`)
- **AES Encryption (`aes_encryption.py`)**: Encrypts payloads with AES-256.
- **RSA Encryption (`rsa_encryption.py`)**: Secure asymmetric encryption implementation.

### Post-Exploitation (`post_exploitation/`)
- **Credential Dump (`credential_dump.py`)**: Extracts credentials from memory.
- **Privilege Escalation (`privilege_escalation.py`)**: Exploits misconfigurations to gain elevated privileges.
- 

## License
This project is licensed under the MIT License.

## Author
Alexander B
