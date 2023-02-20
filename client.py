import requests
from google.protobuf.json_format import MessageToJson, Parse
from mcp.file.v1.file_pb2 import GetFileRequest, GetFileResponse, ListFilesRequest, ListFilesResponse, DeleteFileRequest, DeleteFileResponse, UpdateFileRequest, UpdateFileResponse, Property, Properties, CreateFileResponse
from mcp.operand.v1.operand_pb2 import SearchRequest, SearchResponse, Filter, Condition

class OperandClient:
    """
    Used as a base class to provide common functionality for the various
    operand services exposed throughout this client library.
    """

    def __init__(self, endpoint, key):
        self.key = key
        self.endpoint = endpoint
        if not self.endpoint.endswith("/"):
            self.endpoint += "/"
    
    def _req(self, service, method, body, resp_message, extra_headers=None):
        """
        Makes a request to the service method with the given body.
        Returns the response body, and throws if the response is not 200.
        """
        url = self.endpoint + service + "/" + method
        headers = {"Authorization": "Key "+ self.key, "Content-Type": "application/json"}
        if extra_headers:
            headers.update(extra_headers)
        body = MessageToJson(body, preserving_proto_field_name=True, indent=None)
        resp = requests.post(url, headers=headers, data=body)
        if resp.status_code >= 400:
            raise Exception("Error: " + resp.text)
        elif resp.status_code != 204:
            return Parse(resp.text, resp_message, ignore_unknown_fields=True)

class CreateFileRequest:
    """
    A special multipart-form request to create a file.
    """
    def __init__(self, name, file=None, parent_id=None , properties=None):
        self.name = name 
        # Optional
        self.parent_id = parent_id        
        self.file = file
        self.properties = properties


class FileServiceClient(OperandClient):
    """
    Access the File service, which provides access to the file operations of the API.
    """

    def __init__(self, endpoint, key):
        super().__init__(endpoint, key)
    
    def _req(self, method, body, resp_message):
        return super()._req("file.v1.FileService", method, body, resp_message)
    
    def create_file(self, req: CreateFileRequest) -> CreateFileResponse:
        """
        A special multipart-form request to create a file.
         """
        # If the req.parent is not set, then we need to set it to the root folder.
        if not req.parent_id:
            req.parent_id = ""
        # Construct the multipart form request
        body = {
            "name": req.name,
            "parent_id": req.parent_id,
        }
        if req.properties:
            body["properties"] = MessageToJson(req.properties, preserving_proto_field_name=True, indent=None)

        files = {
            "file": req.file
        }
        headers = {
            "Authorization": "Key "+ self.key
        }
        resp = requests.post(
            self.endpoint + "upload",
            headers=headers,
            data=body,
            files=files
        )
        return resp.json()
        
    
    def get_file(self, req: GetFileRequest) -> GetFileResponse:
        """
        Gets a file.
        """
        return self._req("GetFile", req, GetFileResponse())
    
    def list_files(self, req: ListFilesRequest) -> ListFilesResponse:
        """
        Lists files.
        """
        return self._req("ListFiles", req, ListFilesResponse())
    
    def delete_file(self, req: DeleteFileRequest) -> DeleteFileResponse:
        """
        Deletes a file.
        """
        return self._req("DeleteFile", req, DeleteFileResponse())

    def update_file(self, req: UpdateFileRequest) -> UpdateFileResponse:
        """
        Updates a file.
        """
        return self._req("UpdateFile", req, UpdateFileResponse())


class OperandServiceClient(OperandClient):
    """
    Access the Operand service, which provides access to the main operations of the API.
    """

    def __init__(self, endpoint, key):
        super().__init__(endpoint, key)
    
    def _req(self, method, body, resp_message):
        return super()._req("operand.v1.OperandService", method, body, resp_message)

    def search(self, req: SearchRequest) -> SearchResponse:
        """
        Searches files.
        """
        # If the req.parent is not set, then we need to set it to the root folder.
        if not req.parent_id:
            req.parent_id = ""
        return self._req("Search", req, SearchResponse())


def construct_property_internal(value):
    prop = Property()
    if isinstance(value, str):
        prop.text = value
    elif isinstance(value, int):
        prop.number = float(value)
    elif isinstance(value, float):
        prop.number = value
    elif isinstance(value, list):
        if len(value) == 0:
            raise Exception("Cannot create a property from an empty list")
        first = value[0]
        for v in value:
            if not isinstance(v, type(first)):
                raise Exception("All values in a list must be of the same type")
            if isinstance(v, str):
                prop.text_array.values.append(v)
            elif isinstance(v, int):
                prop.number_array.values.append(float(v))
            elif isinstance(v, float):
                prop.number_array.values.append(v)
            else:
                raise Exception("Invalid value type: " + str(type(v)))
    else:
        raise Exception("Invalid value type: " + str(type(value)))
    return prop

# A utility function to add a property to an object.
# The value can be a string, number, or an array of strings or numbers.
def add_property(obj, key, value):
    prop = construct_property_internal(value)
    if not obj.properties:
        obj.properties = Properties()
    obj.properties.properties[key].CopyFrom(prop)

# A utility function to add a property filter condition to a search filter.
# Essentially, this allows you to filter on a specific value of a property.
def add_property_filter_condition(obj, key, value):
    prop = construct_property_internal(value)
    condition = Condition()
    condition.property.key = key
    condition.property.property.CopyFrom(prop)
    if not obj.filter:
        obj.filter = Filter()
    obj.filter.conditions.append(condition)

# A utility function to add a range condition to a search filter.
# This allows you to filter on a numerical property using comparison operators.
def add_range_condition(obj, key, lt=None, lte=None, gt=None, gte=None):
    condition = Condition()
    condition.range.key = key
    got = False
    if lt is not None and isinstance(lt, (int, float)):
        condition.range.lt = float(lt)
        got = True
    if lte is not None and isinstance(lte, (int, float)):
        condition.range.lte = float(lte)
        got = True
    if gt is not None and isinstance(gt, (int, float)):
        condition.range.gt = float(gt)
        got = True
    if gte is not None and isinstance(gte, (int, float)):
        condition.range.gte = float(gte)
        got = True
    if not got:
        raise Exception("Must specify at least one of lt, lte, gt, or gte")
    if not obj.filter:
        obj.filter = Filter()
    obj.filter.conditions.append(condition)