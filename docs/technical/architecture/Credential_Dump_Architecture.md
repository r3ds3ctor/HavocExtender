# Credential Dump Module Architecture

## Overview
The Credential Dump module extracts credentials from a compromised system, including password hashes and saved credentials.

## Components
- **SAM Dump**: Extracts password hashes from the SAM database.
- **LSASS Dump**: Extracts credentials from LSASS memory.
- **Browser Credentials**: Extracts saved credentials from web browsers.

## Workflow
1. The module extracts credentials from the SAM database, LSASS memory, or web browsers.
2. It stores the credentials for later use.

## Dependencies
- **Python**: The module is written in Python.
- **Impacket**: Used for SAM and LSASS dumping.
- **LaZagne**: Used for browser credential extraction.

## Limitations
- Only works on Windows systems.
- Requires administrative privileges for some operations.