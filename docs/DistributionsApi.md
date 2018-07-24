# swagger_client.DistributionsApi

All URIs are relative to *http://localhost:8000/pulp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**distributions_create**](DistributionsApi.md#distributions_create) | **POST** /distributions/ | 
[**distributions_delete**](DistributionsApi.md#distributions_delete) | **DELETE** /{distribution_href}/ | 
[**distributions_list**](DistributionsApi.md#distributions_list) | **GET** /distributions/ | 
[**distributions_partial_update**](DistributionsApi.md#distributions_partial_update) | **PATCH** /{distribution_href}/ | 
[**distributions_read**](DistributionsApi.md#distributions_read) | **GET** /{distribution_href}/ | 
[**distributions_update**](DistributionsApi.md#distributions_update) | **PUT** /{distribution_href}/ | 


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
> distributions_delete(distribution_href)





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
distribution_href = 'distribution_href_example' # str | URI of Distribution. e.g.: /distributions/1/

try:
    api_instance.distributions_delete(distribution_href)
except ApiException as e:
    print("Exception when calling DistributionsApi->distributions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_href** | **str**| URI of Distribution. e.g.: /distributions/1/ | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributions_list**
> InlineResponse2001 distributions_list(cursor=cursor, page_size=page_size)





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
cursor = 'cursor_example' # str | The pagination cursor value. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.distributions_list(cursor=cursor, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionsApi->distributions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributions_partial_update**
> Distribution distributions_partial_update(distribution_href, data)





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
distribution_href = 'distribution_href_example' # str | URI of Distribution. e.g.: /distributions/1/
data = swagger_client.Distribution() # Distribution | 

try:
    api_response = api_instance.distributions_partial_update(distribution_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionsApi->distributions_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_href** | **str**| URI of Distribution. e.g.: /distributions/1/ | 
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
> Distribution distributions_read(distribution_href)





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
distribution_href = 'distribution_href_example' # str | URI of Distribution. e.g.: /distributions/1/

try:
    api_response = api_instance.distributions_read(distribution_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionsApi->distributions_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_href** | **str**| URI of Distribution. e.g.: /distributions/1/ | 

### Return type

[**Distribution**](Distribution.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributions_update**
> Distribution distributions_update(distribution_href, data)





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
distribution_href = 'distribution_href_example' # str | URI of Distribution. e.g.: /distributions/1/
data = swagger_client.Distribution() # Distribution | 

try:
    api_response = api_instance.distributions_update(distribution_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionsApi->distributions_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_href** | **str**| URI of Distribution. e.g.: /distributions/1/ | 
 **data** | [**Distribution**](Distribution.md)|  | 

### Return type

[**Distribution**](Distribution.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

