# swagger_client.RepositoriesApi

All URIs are relative to *http://localhost:8000/pulp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**repositories_create**](RepositoriesApi.md#repositories_create) | **POST** /repositories/ | 
[**repositories_delete**](RepositoriesApi.md#repositories_delete) | **DELETE** /{repository_href}/ | 
[**repositories_list**](RepositoriesApi.md#repositories_list) | **GET** /repositories/ | 
[**repositories_partial_update**](RepositoriesApi.md#repositories_partial_update) | **PATCH** /{repository_href}/ | 
[**repositories_read**](RepositoriesApi.md#repositories_read) | **GET** /{repository_href}/ | 
[**repositories_update**](RepositoriesApi.md#repositories_update) | **PUT** /{repository_href}/ | 
[**repositories_versions_added_content**](RepositoriesApi.md#repositories_versions_added_content) | **GET** /{repository_version_href}/added_content/ | 
[**repositories_versions_content**](RepositoriesApi.md#repositories_versions_content) | **GET** /{repository_version_href}/content/ | 
[**repositories_versions_create**](RepositoriesApi.md#repositories_versions_create) | **POST** /{repository_version_href}/versions/ | 
[**repositories_versions_delete**](RepositoriesApi.md#repositories_versions_delete) | **DELETE** /{repository_version_href}/ | 
[**repositories_versions_list**](RepositoriesApi.md#repositories_versions_list) | **GET** /{repository_version_href}/versions/ | 
[**repositories_versions_partial_update**](RepositoriesApi.md#repositories_versions_partial_update) | **PATCH** /{repository_version_href}/ | 
[**repositories_versions_read**](RepositoriesApi.md#repositories_versions_read) | **GET** /{repository_version_href}/ | 
[**repositories_versions_removed_content**](RepositoriesApi.md#repositories_versions_removed_content) | **GET** /{repository_version_href}/removed_content/ | 
[**repositories_versions_update**](RepositoriesApi.md#repositories_versions_update) | **PUT** /{repository_version_href}/ | 


# **repositories_create**
> Repository repositories_create(data)





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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
data = swagger_client.Repository() # Repository | 

try:
    api_response = api_instance.repositories_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Repository**](Repository.md)|  | 

### Return type

[**Repository**](Repository.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_delete**
> AsnycOperationResponse repositories_delete(repository_href)



Trigger an asynchronous task to delete a repository.

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
repository_href = 'repository_href_example' # str | URI of Repository. e.g.: /repositories/1/

try:
    api_response = api_instance.repositories_delete(repository_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_href** | **str**| URI of Repository. e.g.: /repositories/1/ | 

### Return type

[**AsnycOperationResponse**](AsnycOperationResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_list**
> InlineResponse2005 repositories_list(cursor=cursor, page_size=page_size)





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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | The pagination cursor value. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.repositories_list(cursor=cursor, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_partial_update**
> Repository repositories_partial_update(repository_href, data)





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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
repository_href = 'repository_href_example' # str | URI of Repository. e.g.: /repositories/1/
data = swagger_client.Repository() # Repository | 

try:
    api_response = api_instance.repositories_partial_update(repository_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_href** | **str**| URI of Repository. e.g.: /repositories/1/ | 
 **data** | [**Repository**](Repository.md)|  | 

### Return type

[**Repository**](Repository.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_read**
> Repository repositories_read(repository_href)





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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
repository_href = 'repository_href_example' # str | URI of Repository. e.g.: /repositories/1/

try:
    api_response = api_instance.repositories_read(repository_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_href** | **str**| URI of Repository. e.g.: /repositories/1/ | 

### Return type

[**Repository**](Repository.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_update**
> AsnycOperationResponse repositories_update(repository_href, data)



Trigger an asynchronous task to updatea repository.

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
repository_href = 'repository_href_example' # str | URI of Repository. e.g.: /repositories/1/
data = swagger_client.Repository() # Repository | 

try:
    api_response = api_instance.repositories_update(repository_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_href** | **str**| URI of Repository. e.g.: /repositories/1/ | 
 **data** | [**Repository**](Repository.md)|  | 

### Return type

[**AsnycOperationResponse**](AsnycOperationResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_versions_added_content**
> Content repositories_versions_added_content(repository_version_href)



List added Content

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
repository_version_href = 'repository_version_href_example' # str | URI of Repository Version. e.g.: /repositories/1/versions/1/

try:
    api_response = api_instance.repositories_versions_added_content(repository_version_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_versions_added_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_version_href** | **str**| URI of Repository Version. e.g.: /repositories/1/versions/1/ | 

### Return type

[**Content**](Content.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_versions_content**
> Content repositories_versions_content(repository_version_href)



List Content

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
repository_version_href = 'repository_version_href_example' # str | URI of Repository Version. e.g.: /repositories/1/versions/1/

try:
    api_response = api_instance.repositories_versions_content(repository_version_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_versions_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_version_href** | **str**| URI of Repository Version. e.g.: /repositories/1/versions/1/ | 

### Return type

[**Content**](Content.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_versions_create**
> AsnycOperationResponse repositories_versions_create(repository_version_href, data)



Trigger an asynchronous task to create a new repository version.

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
repository_version_href = 'repository_version_href_example' # str | URI of Repository Version. e.g.: /repositories/1/versions/
data = swagger_client.RepositoryVersion() # RepositoryVersion | 

try:
    api_response = api_instance.repositories_versions_create(repository_version_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_versions_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_version_href** | **str**| URI of Repository Version. e.g.: /repositories/1/versions/ | 
 **data** | [**RepositoryVersion**](RepositoryVersion.md)|  | 

### Return type

[**AsnycOperationResponse**](AsnycOperationResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_versions_delete**
> AsnycOperationResponse repositories_versions_delete(repository_version_href)



Trigger an asynchronous task to delete a repositroy version.

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
repository_version_href = 'repository_version_href_example' # str | URI of Repository Version. e.g.: /repositories/1/versions/1/

try:
    api_response = api_instance.repositories_versions_delete(repository_version_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_versions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_version_href** | **str**| URI of Repository Version. e.g.: /repositories/1/versions/1/ | 

### Return type

[**AsnycOperationResponse**](AsnycOperationResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_versions_list**
> InlineResponse2006 repositories_versions_list(repository_version_href, ordering=ordering, cursor=cursor, page_size=page_size)





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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
repository_version_href = 'repository_version_href_example' # str | URI of Repository Version. e.g.: /repositories/1/versions/
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
cursor = 'cursor_example' # str | The pagination cursor value. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.repositories_versions_list(repository_version_href, ordering=ordering, cursor=cursor, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_versions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_version_href** | **str**| URI of Repository Version. e.g.: /repositories/1/versions/ | 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_versions_partial_update**
> RepositoryVersion repositories_versions_partial_update(repository_version_href, data)





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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
repository_version_href = 'repository_version_href_example' # str | URI of Repository Version. e.g.: /repositories/1/versions/1/
data = swagger_client.RepositoryVersion() # RepositoryVersion | 

try:
    api_response = api_instance.repositories_versions_partial_update(repository_version_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_versions_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_version_href** | **str**| URI of Repository Version. e.g.: /repositories/1/versions/1/ | 
 **data** | [**RepositoryVersion**](RepositoryVersion.md)|  | 

### Return type

[**RepositoryVersion**](RepositoryVersion.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_versions_read**
> RepositoryVersion repositories_versions_read(repository_version_href)





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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
repository_version_href = 'repository_version_href_example' # str | URI of Repository Version. e.g.: /repositories/1/versions/1/

try:
    api_response = api_instance.repositories_versions_read(repository_version_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_versions_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_version_href** | **str**| URI of Repository Version. e.g.: /repositories/1/versions/1/ | 

### Return type

[**RepositoryVersion**](RepositoryVersion.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_versions_removed_content**
> Content repositories_versions_removed_content(repository_version_href)



List removed Content

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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
repository_version_href = 'repository_version_href_example' # str | URI of Repository Version. e.g.: /repositories/1/versions/1/

try:
    api_response = api_instance.repositories_versions_removed_content(repository_version_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_versions_removed_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_version_href** | **str**| URI of Repository Version. e.g.: /repositories/1/versions/1/ | 

### Return type

[**Content**](Content.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_versions_update**
> RepositoryVersion repositories_versions_update(repository_version_href, data)





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
api_instance = swagger_client.RepositoriesApi(swagger_client.ApiClient(configuration))
repository_version_href = 'repository_version_href_example' # str | URI of Repository Version. e.g.: /repositories/1/versions/1/
data = swagger_client.RepositoryVersion() # RepositoryVersion | 

try:
    api_response = api_instance.repositories_versions_update(repository_version_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_versions_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_version_href** | **str**| URI of Repository Version. e.g.: /repositories/1/versions/1/ | 
 **data** | [**RepositoryVersion**](RepositoryVersion.md)|  | 

### Return type

[**RepositoryVersion**](RepositoryVersion.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

