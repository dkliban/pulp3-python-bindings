# swagger_client.PublishersApi

All URIs are relative to *http://localhost:8000/pulp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publishers_file_create**](PublishersApi.md#publishers_file_create) | **POST** /publishers/file/ | 
[**publishers_file_delete**](PublishersApi.md#publishers_file_delete) | **DELETE** /publishers/file/{id}/ | 
[**publishers_file_list**](PublishersApi.md#publishers_file_list) | **GET** /publishers/file/ | 
[**publishers_file_partial_update**](PublishersApi.md#publishers_file_partial_update) | **PATCH** /publishers/file/{id}/ | 
[**publishers_file_publish**](PublishersApi.md#publishers_file_publish) | **POST** /publishers/file/{id}/publish/ | 
[**publishers_file_read**](PublishersApi.md#publishers_file_read) | **GET** /publishers/file/{id}/ | 
[**publishers_file_update**](PublishersApi.md#publishers_file_update) | **PUT** /publishers/file/{id}/ | 


# **publishers_file_create**
> FilePublisher publishers_file_create(data)





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
api_instance = swagger_client.PublishersApi(swagger_client.ApiClient(configuration))
data = swagger_client.FilePublisher() # FilePublisher | 

try:
    api_response = api_instance.publishers_file_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublishersApi->publishers_file_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**FilePublisher**](FilePublisher.md)|  | 

### Return type

[**FilePublisher**](FilePublisher.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_file_delete**
> publishers_file_delete(id)



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
api_instance = swagger_client.PublishersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this file publisher.

try:
    api_instance.publishers_file_delete(id)
except ApiException as e:
    print("Exception when calling PublishersApi->publishers_file_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this file publisher. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_file_list**
> InlineResponse2004 publishers_file_list(name=name, name__in=name__in, last_updated__lt=last_updated__lt, last_updated__lte=last_updated__lte, last_updated__gt=last_updated__gt, last_updated__gte=last_updated__gte, last_updated__range=last_updated__range, last_updated=last_updated, cursor=cursor)





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
api_instance = swagger_client.PublishersApi(swagger_client.ApiClient(configuration))
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
    api_response = api_instance.publishers_file_list(name=name, name__in=name__in, last_updated__lt=last_updated__lt, last_updated__lte=last_updated__lte, last_updated__gt=last_updated__gt, last_updated__gte=last_updated__gte, last_updated__range=last_updated__range, last_updated=last_updated, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublishersApi->publishers_file_list: %s\n" % e)
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

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_file_partial_update**
> FilePublisher publishers_file_partial_update(id, data)





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
api_instance = swagger_client.PublishersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this file publisher.
data = swagger_client.FilePublisher() # FilePublisher | 

try:
    api_response = api_instance.publishers_file_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublishersApi->publishers_file_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this file publisher. | 
 **data** | [**FilePublisher**](FilePublisher.md)|  | 

### Return type

[**FilePublisher**](FilePublisher.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_file_publish**
> RepositoryPublishURL publishers_file_publish(id, data)



Publishes a repository. Either the ``repository`` or the ``repository_version`` fields can be provided but not both at the same time.

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
api_instance = swagger_client.PublishersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this file publisher.
data = swagger_client.RepositoryPublishURL() # RepositoryPublishURL | 

try:
    api_response = api_instance.publishers_file_publish(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublishersApi->publishers_file_publish: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this file publisher. | 
 **data** | [**RepositoryPublishURL**](RepositoryPublishURL.md)|  | 

### Return type

[**RepositoryPublishURL**](RepositoryPublishURL.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_file_read**
> FilePublisher publishers_file_read(id)





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
api_instance = swagger_client.PublishersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this file publisher.

try:
    api_response = api_instance.publishers_file_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublishersApi->publishers_file_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this file publisher. | 

### Return type

[**FilePublisher**](FilePublisher.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_file_update**
> FilePublisher publishers_file_update(id, data)





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
api_instance = swagger_client.PublishersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A UUID string identifying this file publisher.
data = swagger_client.FilePublisher() # FilePublisher | 

try:
    api_response = api_instance.publishers_file_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublishersApi->publishers_file_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this file publisher. | 
 **data** | [**FilePublisher**](FilePublisher.md)|  | 

### Return type

[**FilePublisher**](FilePublisher.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

