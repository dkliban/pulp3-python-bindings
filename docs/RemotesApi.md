# swagger_client.RemotesApi

All URIs are relative to *http://localhost:8000/pulp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remotes_file_create**](RemotesApi.md#remotes_file_create) | **POST** /remotes/file/ | 
[**remotes_file_delete**](RemotesApi.md#remotes_file_delete) | **DELETE** /remotes/file/{id}/ | 
[**remotes_file_list**](RemotesApi.md#remotes_file_list) | **GET** /remotes/file/ | 
[**remotes_file_partial_update**](RemotesApi.md#remotes_file_partial_update) | **PATCH** /remotes/file/{id}/ | 
[**remotes_file_read**](RemotesApi.md#remotes_file_read) | **GET** /remotes/file/{id}/ | 
[**remotes_file_sync**](RemotesApi.md#remotes_file_sync) | **POST** /remotes/file/{id}/sync/ | 
[**remotes_file_update**](RemotesApi.md#remotes_file_update) | **PUT** /remotes/file/{id}/ | 


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
> remotes_file_delete(id)



Delete a model instance

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
id = 'id_example' # str | A UUID string identifying this file remote.

try:
    api_instance.remotes_file_delete(id)
except ApiException as e:
    print("Exception when calling RemotesApi->remotes_file_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this file remote. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_file_list**
> InlineResponse2005 remotes_file_list(name=name, name__in=name__in, last_updated__lt=last_updated__lt, last_updated__lte=last_updated__lte, last_updated__gt=last_updated__gt, last_updated__gte=last_updated__gte, last_updated__range=last_updated__range, last_updated=last_updated, cursor=cursor)





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
name = 'name_example' # str |  (optional)
name__in = 'name__in_example' # str | Multiple values may be separated by commas. (optional)
last_updated__lt = 'last_updated__lt_example' # str |  (optional)
last_updated__lte = 'last_updated__lte_example' # str |  (optional)
last_updated__gt = 'last_updated__gt_example' # str |  (optional)
last_updated__gte = 'last_updated__gte_example' # str |  (optional)
last_updated__range = 'last_updated__range_example' # str | Multiple values may be separated by commas. (optional)
last_updated = 'last_updated_example' # str |  (optional)
cursor = 'cursor_example' # str | The pagination cursor value. (optional)

try:
    api_response = api_instance.remotes_file_list(name=name, name__in=name__in, last_updated__lt=last_updated__lt, last_updated__lte=last_updated__lte, last_updated__gt=last_updated__gt, last_updated__gte=last_updated__gte, last_updated__range=last_updated__range, last_updated=last_updated, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemotesApi->remotes_file_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **name__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **last_updated__lt** | **str**|  | [optional] 
 **last_updated__lte** | **str**|  | [optional] 
 **last_updated__gt** | **str**|  | [optional] 
 **last_updated__gte** | **str**|  | [optional] 
 **last_updated__range** | **str**| Multiple values may be separated by commas. | [optional] 
 **last_updated** | **str**|  | [optional] 
 **cursor** | **str**| The pagination cursor value. | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_file_partial_update**
> FileRemote remotes_file_partial_update(id, data)





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
id = 'id_example' # str | A UUID string identifying this file remote.
data = swagger_client.FileRemote() # FileRemote | 

try:
    api_response = api_instance.remotes_file_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemotesApi->remotes_file_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this file remote. | 
 **data** | [**FileRemote**](FileRemote.md)|  | 

### Return type

[**FileRemote**](FileRemote.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_file_read**
> FileRemote remotes_file_read(id)





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
id = 'id_example' # str | A UUID string identifying this file remote.

try:
    api_response = api_instance.remotes_file_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemotesApi->remotes_file_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this file remote. | 

### Return type

[**FileRemote**](FileRemote.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_file_sync**
> RepositorySyncURL remotes_file_sync(id, data)



Synchronizes a repository. The ``repository`` field has to be provided.

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
id = 'id_example' # str | A UUID string identifying this file remote.
data = swagger_client.RepositorySyncURL() # RepositorySyncURL | 

try:
    api_response = api_instance.remotes_file_sync(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemotesApi->remotes_file_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this file remote. | 
 **data** | [**RepositorySyncURL**](RepositorySyncURL.md)|  | 

### Return type

[**RepositorySyncURL**](RepositorySyncURL.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_file_update**
> FileRemote remotes_file_update(id, data)





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
id = 'id_example' # str | A UUID string identifying this file remote.
data = swagger_client.FileRemote() # FileRemote | 

try:
    api_response = api_instance.remotes_file_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemotesApi->remotes_file_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this file remote. | 
 **data** | [**FileRemote**](FileRemote.md)|  | 

### Return type

[**FileRemote**](FileRemote.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

