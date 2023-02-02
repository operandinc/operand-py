Official client library for Operand, written in Python.

This library includes a subset of our API, tailored for API-first use cases. For support, or to request additional functionality within this client library, please email us at support@operand.ai or join our Discord server (https://operand.ai/discord).

## Usage

A few simple examples of common usage patterns.

```bash
pip install operand
```

### Required Imports (for Below Examples)

```python
from operand.client import FileServiceClient, OperandServiceClient, CreateFileRequest, CreateFileResponse, add_property, add_property_filter_condition, add_range_condition
from operand.mcp.operand.v1.operand_pb2 import SearchRequest, SearchResponse
```

### Creating a folder

```python
client = FileServiceClient("https://mcp.operand.ai/","API_KEY")
req = CreateFileRequest(
    # Names must be unique within a given folder
    name="cool folder",
)
resp = client.create_file(req)
print(resp)
```

### Uploading a file

```python
client = FileServiceClient("https://mcp.operand.ai/","API_KEY")
req = CreateFileRequest(
    # Names must be unique within a given folder
    name="test.txt",
    # The file contents as bytes
    file=bytes("test", "utf-8")
)
add_property(req, "my-property", "my-value")
add_property(req, "my-number", 123)
add_property(req, "my-number-array", [1, 2, 3])
add_property(req, "my-text-array", ["a", "b", "c"])

resp = client.create_file(req)
print(resp)
```

### Doing a Semantic Search over an Index (with Optional Filters)

```python
client = OperandServiceClient("https://mcp.operand.ai/","API_KEY")
req = SearchRequest()
req.query = "test"
add_property_filter_condition(req, "my-number-array", 3)
add_range_condition(req, "my-number", gt=10)
resp = oclient.search(req)
print(resp)
```
