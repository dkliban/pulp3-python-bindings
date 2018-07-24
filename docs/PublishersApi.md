# swagger_client.PublishersApi

All URIs are relative to *http://localhost:8000/pulp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publishers_file_create**](PublishersApi.md#publishers_file_create) | **POST** /publishers/file/ | 
[**publishers_file_delete**](PublishersApi.md#publishers_file_delete) | **DELETE** /{file_publisher_href}/ | 
[**publishers_file_list**](PublishersApi.md#publishers_file_list) | **GET** /publishers/file/ | 
[**publishers_file_partial_update**](PublishersApi.md#publishers_file_partial_update) | **PATCH** /{file_publisher_href}/ | 
[**publishers_file_publish**](PublishersApi.md#publishers_file_publish) | **POST** /{file_publisher_href}/publish/ | 
[**publishers_file_read**](PublishersApi.md#publishers_file_read) | **GET** /{file_publisher_href}/ | 
[**publishers_file_update**](PublishersApi.md#publishers_file_update) | **PUT** /{file_publisher_href}/ | 


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
> AsnycOperationResponse publishers_file_delete(file_publisher_href)



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
api_instance = swagger_client.PublishersApi(swagger_client.ApiClient(configuration))
file_publisher_href = 'file_publisher_href_example' # str | URI of File Publisher. e.g.: /publishers/file/1/

try:
    api_response = api_instance.publishers_file_delete(file_publisher_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublishersApi->publishers_file_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_publisher_href** | **str**| URI of File Publisher. e.g.: /publishers/file/1/ | 

### Return type

[**AsnycOperationResponse**](AsnycOperationResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_file_list**
> InlineResponse2003 publishers_file_list(cursor=cursor, page_size=page_size)





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
cursor = 'cursor_example' # str | The pagination cursor value. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.publishers_file_list(cursor=cursor, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublishersApi->publishers_file_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_file_partial_update**
> AsnycOperationResponse publishers_file_partial_update(file_publisher_href, data)



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
api_instance = swagger_client.PublishersApi(swagger_client.ApiClient(configuration))
file_publisher_href = 'file_publisher_href_example' # str | URI of File Publisher. e.g.: /publishers/file/1/
data = swagger_client.FilePublisher() # FilePublisher | 

try:
    api_response = api_instance.publishers_file_partial_update(file_publisher_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublishersApi->publishers_file_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_publisher_href** | **str**| URI of File Publisher. e.g.: /publishers/file/1/ | 
 **data** | [**FilePublisher**](FilePublisher.md)|  | 

### Return type

[**AsnycOperationResponse**](AsnycOperationResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_file_publish**
> AsnycOperationResponse publishers_file_publish(file_publisher_href, data)



Trigger an asynchronous task to publish file content.

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
file_publisher_href = 'file_publisher_href_example' # str | URI of File Publisher. e.g.: /publishers/file/1/
data = swagger_client.RepositoryPublishURL() # RepositoryPublishURL | 

try:
    api_response = api_instance.publishers_file_publish(file_publisher_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublishersApi->publishers_file_publish: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_publisher_href** | **str**| URI of File Publisher. e.g.: /publishers/file/1/ | 
 **data** | [**RepositoryPublishURL**](RepositoryPublishURL.md)|  | 

### Return type

[**AsnycOperationResponse**](AsnycOperationResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_file_read**
> FilePublisher publishers_file_read(file_publisher_href)





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
file_publisher_href = 'file_publisher_href_example' # str | URI of File Publisher. e.g.: /publishers/file/1/

try:
    api_response = api_instance.publishers_file_read(file_publisher_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublishersApi->publishers_file_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_publisher_href** | **str**| URI of File Publisher. e.g.: /publishers/file/1/ | 

### Return type

[**FilePublisher**](FilePublisher.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_file_update**
> AsnycOperationResponse publishers_file_update(file_publisher_href, data)



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
api_instance = swagger_client.PublishersApi(swagger_client.ApiClient(configuration))
file_publisher_href = 'file_publisher_href_example' # str | URI of File Publisher. e.g.: /publishers/file/1/
data = swagger_client.FilePublisher() # FilePublisher | 

try:
    api_response = api_instance.publishers_file_update(file_publisher_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublishersApi->publishers_file_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_publisher_href** | **str**| URI of File Publisher. e.g.: /publishers/file/1/ | 
 **data** | [**FilePublisher**](FilePublisher.md)|  | 

### Return type

[**AsnycOperationResponse**](AsnycOperationResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

