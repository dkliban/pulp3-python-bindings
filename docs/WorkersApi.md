# swagger_client.WorkersApi

All URIs are relative to *http://localhost:8000/pulp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workers_list**](WorkersApi.md#workers_list) | **GET** /workers/ | 
[**workers_read**](WorkersApi.md#workers_read) | **GET** /workers/{id}/ | 


# **workers_list**
> InlineResponse20010 workers_list(name=name, name__in=name__in, last_heartbeat__lt=last_heartbeat__lt, last_heartbeat__lte=last_heartbeat__lte, last_heartbeat__gt=last_heartbeat__gt, last_heartbeat__gte=last_heartbeat__gte, last_heartbeat__range=last_heartbeat__range, online=online, missing=missing, last_heartbeat=last_heartbeat, cursor=cursor)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)
name__in = 'name__in_example' # str | Multiple values may be separated by commas. (optional)
last_heartbeat__lt = 'last_heartbeat__lt_example' # str |  (optional)
last_heartbeat__lte = 'last_heartbeat__lte_example' # str |  (optional)
last_heartbeat__gt = 'last_heartbeat__gt_example' # str |  (optional)
last_heartbeat__gte = 'last_heartbeat__gte_example' # str |  (optional)
last_heartbeat__range = 'last_heartbeat__range_example' # str | Multiple values may be separated by commas. (optional)
online = 'online_example' # str |  (optional)
missing = 'missing_example' # str |  (optional)
last_heartbeat = 'last_heartbeat_example' # str |  (optional)
cursor = 'cursor_example' # str | The pagination cursor value. (optional)

try:
    api_response = api_instance.workers_list(name=name, name__in=name__in, last_heartbeat__lt=last_heartbeat__lt, last_heartbeat__lte=last_heartbeat__lte, last_heartbeat__gt=last_heartbeat__gt, last_heartbeat__gte=last_heartbeat__gte, last_heartbeat__range=last_heartbeat__range, online=online, missing=missing, last_heartbeat=last_heartbeat, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->workers_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **name__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **last_heartbeat__lt** | **str**|  | [optional] 
 **last_heartbeat__lte** | **str**|  | [optional] 
 **last_heartbeat__gt** | **str**|  | [optional] 
 **last_heartbeat__gte** | **str**|  | [optional] 
 **last_heartbeat__range** | **str**| Multiple values may be separated by commas. | [optional] 
 **online** | **str**|  | [optional] 
 **missing** | **str**|  | [optional] 
 **last_heartbeat** | **str**|  | [optional] 
 **cursor** | **str**| The pagination cursor value. | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workers_read**
> Worker workers_read(id)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this worker.

try:
    api_response = api_instance.workers_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->workers_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this worker. | 

### Return type

[**Worker**](Worker.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

