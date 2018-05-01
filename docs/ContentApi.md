# swagger_client.ContentApi

All URIs are relative to *http://localhost:8000/pulp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**content_file_create**](ContentApi.md#content_file_create) | **POST** /content/file/ | 
[**content_file_list**](ContentApi.md#content_file_list) | **GET** /content/file/ | 
[**content_file_read**](ContentApi.md#content_file_read) | **GET** /content/file/{id}/ | 


# **content_file_create**
> FileContent content_file_create(data)





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
api_instance = swagger_client.ContentApi(swagger_client.ApiClient(configuration))
data = swagger_client.FileContent() # FileContent | 

try:
    api_response = api_instance.content_file_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->content_file_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**FileContent**](FileContent.md)|  | 

### Return type

[**FileContent**](FileContent.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_file_list**
> InlineResponse2001 content_file_list(relative_path=relative_path, digest=digest, cursor=cursor)





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
api_instance = swagger_client.ContentApi(swagger_client.ApiClient(configuration))
relative_path = 'relative_path_example' # str |  (optional)
digest = 'digest_example' # str |  (optional)
cursor = 'cursor_example' # str | The pagination cursor value. (optional)

try:
    api_response = api_instance.content_file_list(relative_path=relative_path, digest=digest, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->content_file_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relative_path** | **str**|  | [optional] 
 **digest** | **str**|  | [optional] 
 **cursor** | **str**| The pagination cursor value. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_file_read**
> FileContent content_file_read(id)





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
api_instance = swagger_client.ContentApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this file content.

try:
    api_response = api_instance.content_file_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentApi->content_file_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this file content. | 

### Return type

[**FileContent**](FileContent.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

