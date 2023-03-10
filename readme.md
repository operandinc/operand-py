Official client library for Operand, written in Python.

This library includes a subset of our API, tailored for API-first use cases. For support, or to request additional functionality within this client library, please email us at support@operand.ai or join our Discord server (https://operand.ai/discord).

## Usage

A few simple examples of common usage patterns.

```bash
pip install operand
```

### Required Imports (for Below Examples)

```python
import os
from operand.client import FileServiceClient, OperandServiceClient, CreateFileRequest, add_property, add_property_filter_condition, add_range_condition
from mcp.operand.v1.operand_pb2 import SearchRequest, SearchResponse
from mcp.file.v1.file_pb2 import CreateFileResponse, GetFileRequest, DeleteFileRequest, FileSelector
```

### Creating a folder

```python
client = FileServiceClient("https://mcp.operand.ai", os.getenv("OPERAND_API_KEY"))
req = CreateFileRequest(
    # Names must be unique within a given folder
    name="cool folder",
)
resp = client.create_file(req)
print(resp)
```

### Uploading a file to a specific folder

```python
client = FileServiceClient("https://mcp.operand.ai", os.getenv("OPERAND_API_KEY"))
req = CreateFileRequest(
    # Names must be unique within a given folder
    name="test.txt",
    parent_id="FOLDER_ID",
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

### Searching over a specific folder (with Optional Filters)

```python
client = OperandServiceClient("https://mcp.operand.ai", os.getenv("OPERAND_API_KEY"))
req = SearchRequest()
req.query = "test"
req.parent_id = "FOLDER_ID"
add_property_filter_condition(req, "my-number-array", 3)
add_range_condition(req, "my-number", gt=10)
resp = client.search(req)
print(resp)
```

### Getting a file by ID

```python
client = FileServiceClient("https://mcp.operand.ai", os.getenv("OPERAND_API_KEY"))
# Get a file
req = GetFileRequest(
    selector = FileSelector(
        id = "FILE_ID"
    )
)
resp = client.get_file(req)
print(resp)
```

### Getting a file by name

```python
client = FileServiceClient("https://mcp.operand.ai", os.getenv("OPERAND_API_KEY"))
# Get a file
req = GetFileRequest(
    selector = FileSelector(
        by_name = FileSelector.ByName(
            name = "FILE_NAME",
            parent_id = "" # root folder
        )
    )
)
resp = client.get_file(req)
print(resp)
```

### Deleting a file by ID

```python
client = FileServiceClient("https://mcp.operand.ai", os.getenv("OPERAND_API_KEY"))
# Get a file
req = DeleteFileRequest(
    selector = FileSelector(
       id = "FILE_ID"
    )
)
resp = client.delete_file(req)
print(resp)
```
