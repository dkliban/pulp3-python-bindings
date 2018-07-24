# swagger_client.RemotesApi

All URIs are relative to *http://localhost:8000/pulp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remotes_file_create**](RemotesApi.md#remotes_file_create) | **POST** /remotes/file/ | 
[**remotes_file_delete**](RemotesApi.md#remotes_file_delete) | **DELETE** /{file_remote_href}/ | 
[**remotes_file_list**](RemotesApi.md#remotes_file_list) | **GET** /remotes/file/ | 
[**remotes_file_partial_update**](RemotesApi.md#remotes_file_partial_update) | **PATCH** /{file_remote_href}/ | 
[**remotes_file_read**](RemotesApi.md#remotes_file_read) | **GET** /{file_remote_href}/ | 
[**remotes_file_sync**](RemotesApi.md#remotes_file_sync) | **POST** /{file_remote_href}/sync/ | 
[**remotes_file_update**](RemotesApi.md#remotes_file_update) | **PUT** /{file_remote_href}/ | 


# **remotes_file_create**
> FileRemote remotes_file_create(data)





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
api_instance = swagger_client.RemotesApi(swagger_client.ApiClient(configuration))
data = swagger_client.FileRemote() # FileRemote | 

try:
    api_response = api_instance.remotes_file_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemotesApi->remotes_file_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**FileRemote**](FileRemote.md)|  | 

### Return type

[**FileRemote**](FileRemote.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_file_delete**
> AsnycOperationResponse remotes_file_delete(file_remote_href)



Trigger an asynchronous delete task

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
api_instance = swagger_client.RemotesApi(swagger_client.ApiClient(configuration))
file_remote_href = 'file_remote_href_example' # str | URI of File Remote. e.g.: /remotes/file/1/

try:
    api_response = api_instance.remotes_file_delete(file_remote_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemotesApi->remotes_file_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_remote_href** | **str**| URI of File Remote. e.g.: /remotes/file/1/ | 

### Return type

[**AsnycOperationResponse**](AsnycOperationResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_file_list**
> InlineResponse2004 remotes_file_list(cursor=cursor, page_size=page_size)





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
api_instance = swagger_client.RemotesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | The pagination cursor value. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.remotes_file_list(cursor=cursor, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemotesApi->remotes_file_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_file_partial_update**
> AsnycOperationResponse remotes_file_partial_update(file_remote_href, data)



Trigger an asynchronous partial update task

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
api_instance = swagger_client.RemotesApi(swagger_client.ApiClient(configuration))
file_remote_href = 'file_remote_href_example' # str | URI of File Remote. e.g.: /remotes/file/1/
data = swagger_client.FileRemote() # FileRemote | 

try:
    api_response = api_instance.remotes_file_partial_update(file_remote_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemotesApi->remotes_file_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_remote_href** | **str**| URI of File Remote. e.g.: /remotes/file/1/ | 
 **data** | [**FileRemote**](FileRemote.md)|  | 

### Return type

[**AsnycOperationResponse**](AsnycOperationResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_file_read**
> FileRemote remotes_file_read(file_remote_href)





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
api_instance = swagger_client.RemotesApi(swagger_client.ApiClient(configuration))
file_remote_href = 'file_remote_href_example' # str | URI of File Remote. e.g.: /remotes/file/1/

try:
    api_response = api_instance.remotes_file_read(file_remote_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemotesApi->remotes_file_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_remote_href** | **str**| URI of File Remote. e.g.: /remotes/file/1/ | 

### Return type

[**FileRemote**](FileRemote.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_file_sync**
> AsnycOperationResponse remotes_file_sync(file_remote_href, data)



Trigger an asynchronous task to sync file content.

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
api_instance = swagger_client.RemotesApi(swagger_client.ApiClient(configuration))
file_remote_href = 'file_remote_href_example' # str | URI of File Remote. e.g.: /remotes/file/1/
data = swagger_client.RepositorySyncURL() # RepositorySyncURL | 

try:
    api_response = api_instance.remotes_file_sync(file_remote_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemotesApi->remotes_file_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_remote_href** | **str**| URI of File Remote. e.g.: /remotes/file/1/ | 
 **data** | [**RepositorySyncURL**](RepositorySyncURL.md)|  | 

### Return type

[**AsnycOperationResponse**](AsnycOperationResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_file_update**
> AsnycOperationResponse remotes_file_update(file_remote_href, data)



Trigger an asynchronous update task

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
api_instance = swagger_client.RemotesApi(swagger_client.ApiClient(configuration))
file_remote_href = 'file_remote_href_example' # str | URI of File Remote. e.g.: /remotes/file/1/
data = swagger_client.FileRemote() # FileRemote | 

try:
    api_response = api_instance.remotes_file_update(file_remote_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemotesApi->remotes_file_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_remote_href** | **str**| URI of File Remote. e.g.: /remotes/file/1/ | 
 **data** | [**FileRemote**](FileRemote.md)|  | 

### Return type

[**AsnycOperationResponse**](AsnycOperationResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

