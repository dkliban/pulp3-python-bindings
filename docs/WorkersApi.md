# swagger_client.WorkersApi

All URIs are relative to *http://localhost:8000/pulp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workers_list**](WorkersApi.md#workers_list) | **GET** /workers/ | 
[**workers_read**](WorkersApi.md#workers_read) | **GET** /{worker_href}/ | 


# **workers_list**
> InlineResponse2009 workers_list(cursor=cursor, page_size=page_size)





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
cursor = 'cursor_example' # str | The pagination cursor value. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.workers_list(cursor=cursor, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->workers_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workers_read**
> Worker workers_read(worker_href)





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
worker_href = 'worker_href_example' # str | URI of Worker. e.g.: /workers/1/

try:
    api_response = api_instance.workers_read(worker_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->workers_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **worker_href** | **str**| URI of Worker. e.g.: /workers/1/ | 

### Return type

[**Worker**](Worker.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

