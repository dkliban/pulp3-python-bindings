# swagger_client.ArtifactsApi

All URIs are relative to *http://localhost:8000/pulp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**artifacts_create**](ArtifactsApi.md#artifacts_create) | **POST** /artifacts/ | 
[**artifacts_delete**](ArtifactsApi.md#artifacts_delete) | **DELETE** {href} | 
[**artifacts_list**](ArtifactsApi.md#artifacts_list) | **GET** /artifacts/ | 
[**artifacts_read**](ArtifactsApi.md#artifacts_read) | **GET** {href} | 


# **artifacts_create**
> Artifact artifacts_create(data)





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
api_instance = swagger_client.ArtifactsApi(swagger_client.ApiClient(configuration))
data = swagger_client.Artifact() # Artifact | 

try:
    api_response = api_instance.artifacts_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->artifacts_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Artifact**](Artifact.md)|  | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artifacts_delete**
> artifacts_delete(href)



Remove Artifact only if it is not associated with any Content.

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
api_instance = swagger_client.ArtifactsApi(swagger_client.ApiClient(configuration))
href = 'id_example' # str | A relative URI for the resource.

try:
    api_instance.artifacts_delete(href)
except ApiException as e:
    print("Exception when calling ArtifactsApi->artifacts_delete: %s\n" % e)
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

# **artifacts_list**
> InlineResponse200 artifacts_list(md5=md5, sha1=sha1, sha224=sha224, sha256=sha256, sha384=sha384, sha512=sha512, cursor=cursor)





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
api_instance = swagger_client.ArtifactsApi(swagger_client.ApiClient(configuration))
md5 = 'md5_example' # str |  (optional)
sha1 = 'sha1_example' # str |  (optional)
sha224 = 'sha224_example' # str |  (optional)
sha256 = 'sha256_example' # str |  (optional)
sha384 = 'sha384_example' # str |  (optional)
sha512 = 'sha512_example' # str |  (optional)
cursor = 'cursor_example' # str | The pagination cursor value. (optional)

try:
    api_response = api_instance.artifacts_list(md5=md5, sha1=sha1, sha224=sha224, sha256=sha256, sha384=sha384, sha512=sha512, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->artifacts_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **md5** | **str**|  | [optional] 
 **sha1** | **str**|  | [optional] 
 **sha224** | **str**|  | [optional] 
 **sha256** | **str**|  | [optional] 
 **sha384** | **str**|  | [optional] 
 **sha512** | **str**|  | [optional] 
 **cursor** | **str**| The pagination cursor value. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artifacts_read**
> Artifact artifacts_read(href)





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
api_instance = swagger_client.ArtifactsApi(swagger_client.ApiClient(configuration))
href = 'id_example' # str | A relative URI for the resource.

try:
    api_response = api_instance.artifacts_read(href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->artifacts_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **href** | [**str**](.md)| A relative URI for the resource. | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

