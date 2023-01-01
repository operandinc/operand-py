Official client library for Operand, written in Python.

This library includes a subset of our API, tailored for API-first use cases. For support, or to request additional functionality within this client library, please email us at support@operand.ai or join our Discord server (https://operand.ai/discord).

## Usage

A few simple examples of common usage patterns.

```bash
pip install operand
```

### Required Imports (for Below Examples)

```python
from operand.client import IndexClient, ObjectService, add_property, add_property_filter_condition, add_range_condition
from operand.v1.index_pb2 import CreateIndexRequest
from operand.v1.object_pb2 import ObjectType, UpsertRequest, SearchWithinRequest
```

### Creating an Index

```python
client = IndexClient("https://api.operand.ai", "<your-api-key>")
req = CreateIndexRequest()
req.name = "my-index"
req.description = "Created by Python"
req.public = False
resp = client.create_index(req)
print(resp.index.public_id)
```

### Indexing A Text Object with Properties

```python
objectClient = ObjectService("https://api.operand.ai", "<your api key>", resp.index.public_id)
req = UpsertRequest()
req.type = ObjectType.OBJECT_TYPE_TEXT
req.metadata.text.text = "Hello world"
add_property(req, "my-property", "my-value")
add_property(req, "my-number", 123)
add_property(req, "my-number-array", [1, 2, 3])
add_property(req, "my-text-array", ["a", "b", "c"])
resp = objectClient.upsert(req)
print(resp)
```

### Doing a Semantic Search over an Index (with Optional Filters)

```python
req = SearchWithinRequest()
req.query = "hello"
add_property_filter_condition(req, "my-number-array", 3)
add_range_condition(req, "my-number", gt=10)
resp = objectClient.search_within(req)
print(resp)
```
