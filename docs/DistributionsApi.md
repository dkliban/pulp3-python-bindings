# swagger_client.DistributionsApi

All URIs are relative to *http://localhost:8000/pulp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**distributions_create**](DistributionsApi.md#distributions_create) | **POST** /distributions/ | 
[**distributions_delete**](DistributionsApi.md#distributions_delete) | **DELETE** {href} | 
[**distributions_list**](DistributionsApi.md#distributions_list) | **GET** /distributions/ | 
[**distributions_partial_update**](DistributionsApi.md#distributions_partial_update) | **PATCH** {href} | 
[**distributions_read**](DistributionsApi.md#distributions_read) | **GET** {href} | 
[**distributions_update**](DistributionsApi.md#distributions_update) | **PUT** {href} | 


# **distributions_create**
> Distribution distributions_create(data)





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
api_instance = swagger_client.DistributionsApi(swagger_client.ApiClient(configuration))
data = swagger_client.Distribution() # Distribution | 

try:
    api_response = api_instance.distributions_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionsApi->distributions_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Distribution**](Distribution.md)|  | 

### Return type

[**Distribution**](Distribution.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributions_delete**
> distributions_delete(href)





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
api_instance = swagger_client.DistributionsApi(swagger_client.ApiClient(configuration))
href = 'id_example' # str | A relative URI for the resource.

try:
    api_instance.distributions_delete(href)
except ApiException as e:
    print("Exception when calling DistributionsApi->distributions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **href** | [**str**](.md)| A relative URI for the resource. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributions_list**
> InlineResponse2002 distributions_list(name=name, name__in=name__in, base_path=base_path, base_path__contains=base_path__contains, base_path__icontains=base_path__icontains, base_path__in=base_path__in, cursor=cursor)





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
api_instance = swagger_client.DistributionsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)
name__in = 'name__in_example' # str | Multiple values may be separated by commas. (optional)
base_path = 'base_path_example' # str |  (optional)
base_path__contains = 'base_path__contains_example' # str |  (optional)
base_path__icontains = 'base_path__icontains_example' # str |  (optional)
base_path__in = 'base_path__in_example' # str | Multiple values may be separated by commas. (optional)
cursor = 'cursor_example' # str | The pagination cursor value. (optional)

try:
    api_response = api_instance.distributions_list(name=name, name__in=name__in, base_path=base_path, base_path__contains=base_path__contains, base_path__icontains=base_path__icontains, base_path__in=base_path__in, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionsApi->distributions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **name__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **base_path** | **str**|  | [optional] 
 **base_path__contains** | **str**|  | [optional] 
 **base_path__icontains** | **str**|  | [optional] 
 **base_path__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **cursor** | **str**| The pagination cursor value. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributions_partial_update**
> Distribution distributions_partial_update(href, data)





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
api_instance = swagger_client.DistributionsApi(swagger_client.ApiClient(configuration))
href = 'id_example' # str | A relative URI for the resource.
data = swagger_client.Distribution() # Distribution | 

try:
    api_response = api_instance.distributions_partial_update(href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionsApi->distributions_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **href** | [**str**](.md)| A relative URI for the resource. | 
 **data** | [**Distribution**](Distribution.md)|  | 

### Return type

[**Distribution**](Distribution.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributions_read**
> Distribution distributions_read(href)





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
api_instance = swagger_client.DistributionsApi(swagger_client.ApiClient(configuration))
href = 'id_example' # str | A relative URI for the resource.

try:
    api_response = api_instance.distributions_read(href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionsApi->distributions_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **href** | [**str**](.md)| A relative URI for the resource. | 

### Return type

[**Distribution**](Distribution.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributions_update**
> Distribution distributions_update(href, data)





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
api_instance = swagger_client.DistributionsApi(swagger_client.ApiClient(configuration))
href = 'id_example' # str | A relative URI for the resource.
data = swagger_client.Distribution() # Distribution | 

try:
    api_response = api_instance.distributions_update(href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionsApi->distributions_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **href** | [**str**](.md)| A relative URI for the resource. | 
 **data** | [**Distribution**](Distribution.md)|  | 

### Return type

[**Distribution**](Distribution.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

