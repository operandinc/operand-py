import requests
from google.protobuf.json_format import MessageToJson, Parse
from operand.v1.index_pb2 import CreateIndexRequest, CreateIndexResponse, DeleteIndexRequest, DeleteIndexResponse
from operand.v1.object_pb2 import UpsertRequest, UpsertResponse, DeleteRequest, DeleteResponse, SearchWithinRequest, SearchWithinResponse, Properties, Property, Filter, Condition

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
        headers = {"Authorization": self.key, "Content-Type": "application/json"}
        if extra_headers:
            headers.update(extra_headers)
        body = MessageToJson(body, preserving_proto_field_name=True, indent=None)
        resp = requests.post(url, headers=headers, data=body)
        if resp.status_code != 200:
            raise Exception("Operand request failed: " + resp.text)
        return Parse(resp.text, resp_message)


class IndexClient(OperandClient):
    """
    Access the Index service, which allows users to create and manage their indexes.
    """

    def __init__(self, endpoint, key):
        super().__init__(endpoint, key)
    
    def _req(self, method, body, resp_message):
        return super()._req("operand.v1.IndexService", method, body, resp_message)
    
    def create_index(self, req: CreateIndexRequest) -> CreateIndexResponse:
        """
        Creates a new index.
        """
        return self._req("CreateIndex", req, CreateIndexResponse())
    
    def delete_index(self, req: DeleteIndexRequest) -> DeleteIndexResponse:
        """
        Deletes an index.
        """
        return self._req("DeleteIndex", req, DeleteIndexResponse())

class ObjectService(OperandClient):
    """
    Access the Object service, which allows users to manage the contents of an index,
    in addition to performing operations on the index.
    """

    def __init__(self, endpoint, key, index_id):
        super().__init__(endpoint, key)
        self.index_id = index_id
    
    def _req(self, method, body, resp_message):
        return super()._req("operand.v1.ObjectService", method, body, resp_message, {"Operand-Index-ID": self.index_id})
    
    def upsert(self, req: UpsertRequest) -> UpsertResponse:
        """
        Upserts an object into the index.
        """
        return self._req("Upsert", req, UpsertResponse())
    
    def delete(self, req: DeleteRequest) -> DeleteResponse:
        """
        Deletes an object from the index.
        """
        return self._req("Delete", req, DeleteResponse())
    
    def search_within(self, req: SearchWithinRequest) -> SearchWithinResponse:
        """
        Performs a search within the index.
        """
        return self._req("SearchWithin", req, SearchWithinResponse())

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