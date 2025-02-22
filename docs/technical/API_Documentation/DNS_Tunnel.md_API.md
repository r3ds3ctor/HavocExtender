
---

**File**: `DNS_Tunnel_API.md`

```markdown
# DNS Tunnel Module API Documentation

## Functions
### `send_dns_query(domain, data)`
- **Description**: Sends data through a DNS query.
- **Parameters**:
  - `domain`: The domain to send the query to.
  - `data`: The data to send.
- **Returns**: A string indicating success or failure.

### `receive_dns_response(domain)`
- **Description**: Receives data through a DNS response.
- **Parameters**:
  - `domain`: The domain to receive the response from.
- **Returns**: A string indicating success or failure.

## Example Usage
```python
from dns_tunnel import send_dns_query, receive_dns_response

# Send data through a DNS query
result = send_dns_query("example.com", "secret_data")
print(result)

# Receive data through a DNS response
result = receive_dns_response("example.com")
print(result)