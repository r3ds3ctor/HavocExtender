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

## Installation and Usage

1. **Clone the Repository**:
   ```
   git clone https://github.com/yourusername/HavocExtender.git
   cd HavocExtender
     ```
2. **Install Dependencies:**
Ensure you have Python 3.8+ installed. Install required dependencies using:
  ```
pip install -r requirements.txt
  ```
**Configure Havoc C2:**

Ensure Havoc C2 is installed and running.
Copy the modules from the src/ directory to the plugins/ directory of your Havoc C2 installation:

```cp src/*.py /path/to/havoc/plugins/```

3. **Load the Modules in Havoc C2**
Start Havoc C2.

**Use the loadplugin command to load the modules:**

```loadplugin bypass_edr_av.py
loadplugin process_injection.py
loadplugin registry_persistence.py
```
Verify that the modules are loaded by using the help command.

## Using the Modules
Each module comes with its own set of commands. Use the help command to explore the available commands for each module.

**Example: Using the Bypass EDR/AV Module**
Disable AMSI:
```
bypass_amsi
Inject a DLL into a remote process:
```
```
inject_dll 1234 malicious.dll
```
## Troubleshooting
Module Not Loading: Ensure the module files are in the plugins/ directory and that you have the required dependencies installed.
Command Not Found: Verify that the module is loaded using the loadplugin command.
**Run Tests:**
Verify the functionality of the modules by running the test suite:

  ```python -m pytest tests/   ```
## Usage
Load Modules in Havoc C2:

Use the Havoc C2 interface to load the desired modules from the src/ directory.

Configure module parameters as needed.

**Examples:**

For evasion techniques, refer to the examples/bypass_edr_av/ directory.

For persistence, check the examples/persistence/ directory.

## Documentation:
Detailed usage instructions and tutorials are available in the docs/tutorials/ directory. 

## License
This project is licensed under the MIT License.

## Author
Alexander B

## 🤝 Contributing
This project thrives on community contributions. If you'd like to suggest improvements, report issues, or add new features, feel free to open a pull request.  
If you’d like to support future development, you can do so here: 

☕ [buymeacoffee.com/alexboteroh]
