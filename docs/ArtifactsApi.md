# swagger_client.ArtifactsApi

All URIs are relative to *http://localhost:8000/pulp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**artifacts_create**](ArtifactsApi.md#artifacts_create) | **POST** /artifacts/ | 
[**artifacts_delete**](ArtifactsApi.md#artifacts_delete) | **DELETE** /{artifact_href}/ | 
[**artifacts_list**](ArtifactsApi.md#artifacts_list) | **GET** /artifacts/ | 
[**artifacts_read**](ArtifactsApi.md#artifacts_read) | **GET** /{artifact_href}/ | 


# **artifacts_create**
> artifacts_create(file, id=id, href=href, created=created, size=size, md5=md5, sha1=sha1, sha224=sha224, sha256=sha256, sha384=sha384, sha512=sha512)





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
file = '/path/to/file.txt' # file | The stored file.
id = 56 # int |  (optional)
href = 'href_example' # str |  (optional)
created = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of creation. (optional)
size = 56 # int | The size of the file in bytes. (optional)
md5 = 'md5_example' # str | The MD5 checksum of the file if available. (optional)
sha1 = 'sha1_example' # str | The SHA-1 checksum of the file if available. (optional)
sha224 = 'sha224_example' # str | The SHA-224 checksum of the file if available. (optional)
sha256 = 'sha256_example' # str | The SHA-256 checksum of the file if available. (optional)
sha384 = 'sha384_example' # str | The SHA-384 checksum of the file if available. (optional)
sha512 = 'sha512_example' # str | The SHA-512 checksum of the file if available. (optional)

try:
    api_instance.artifacts_create(file, id=id, href=href, created=created, size=size, md5=md5, sha1=sha1, sha224=sha224, sha256=sha256, sha384=sha384, sha512=sha512)
except ApiException as e:
    print("Exception when calling ArtifactsApi->artifacts_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| The stored file. | 
 **id** | **int**|  | [optional] 
 **href** | **str**|  | [optional] 
 **created** | **datetime**| Timestamp of creation. | [optional] 
 **size** | **int**| The size of the file in bytes. | [optional] 
 **md5** | **str**| The MD5 checksum of the file if available. | [optional] 
 **sha1** | **str**| The SHA-1 checksum of the file if available. | [optional] 
 **sha224** | **str**| The SHA-224 checksum of the file if available. | [optional] 
 **sha256** | **str**| The SHA-256 checksum of the file if available. | [optional] 
 **sha384** | **str**| The SHA-384 checksum of the file if available. | [optional] 
 **sha512** | **str**| The SHA-512 checksum of the file if available. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artifacts_delete**
> artifacts_delete(artifact_href)



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
artifact_href = 'artifact_href_example' # str | URI of Artifact. e.g.: /artifacts/1/

try:
    api_instance.artifacts_delete(artifact_href)
except ApiException as e:
    print("Exception when calling ArtifactsApi->artifacts_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_href** | **str**| URI of Artifact. e.g.: /artifacts/1/ | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artifacts_list**
> artifacts_list(cursor=cursor, page_size=page_size)





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
cursor = 'cursor_example' # str | The pagination cursor value. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_instance.artifacts_list(cursor=cursor, page_size=page_size)
except ApiException as e:
    print("Exception when calling ArtifactsApi->artifacts_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artifacts_read**
> artifacts_read(artifact_href)





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
artifact_href = 'artifact_href_example' # str | URI of Artifact. e.g.: /artifacts/1/

try:
    api_instance.artifacts_read(artifact_href)
except ApiException as e:
    print("Exception when calling ArtifactsApi->artifacts_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_href** | **str**| URI of Artifact. e.g.: /artifacts/1/ | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

