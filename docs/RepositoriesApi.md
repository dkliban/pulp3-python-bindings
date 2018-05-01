# swagger_client.RepositoriesApi

All URIs are relative to *http://localhost:8000/pulp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**repositories_create**](RepositoriesApi.md#repositories_create) | **POST** /repositories/ | 
[**repositories_delete**](RepositoriesApi.md#repositories_delete) | **DELETE** /repositories/{id}/ | 
[**repositories_list**](RepositoriesApi.md#repositories_list) | **GET** /repositories/ | 
[**repositories_partial_update**](RepositoriesApi.md#repositories_partial_update) | **PATCH** /repositories/{id}/ | 
[**repositories_read**](RepositoriesApi.md#repositories_read) | **GET** /repositories/{id}/ | 
[**repositories_update**](RepositoriesApi.md#repositories_update) | **PUT** /repositories/{id}/ | 
[**repositories_versions_added_content**](RepositoriesApi.md#repositories_versions_added_content) | **GET** /repositories/{repository_pk}/versions/{number}/added_content/ | 
[**repositories_versions_content**](RepositoriesApi.md#repositories_versions_content) | **GET** /repositories/{repository_pk}/versions/{number}/content/ | 
[**repositories_versions_create**](RepositoriesApi.md#repositories_versions_create) | **POST** /repositories/{repository_pk}/versions/ | 
[**repositories_versions_delete**](RepositoriesApi.md#repositories_versions_delete) | **DELETE** /repositories/{repository_pk}/versions/{number}/ | 
[**repositories_versions_list**](RepositoriesApi.md#repositories_versions_list) | **GET** /repositories/{repository_pk}/versions/ | 
[**repositories_versions_read**](RepositoriesApi.md#repositories_versions_read) | **GET** /repositories/{repository_pk}/versions/{number}/ | 
[**repositories_versions_removed_content**](RepositoriesApi.md#repositories_versions_removed_content) | **GET** /repositories/{repository_pk}/versions/{number}/removed_content/ | 


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
> repositories_delete(id)



Generates a Task to delete a Repository

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
id = 'id_example' # str | A UUID string identifying this repository.

try:
    api_instance.repositories_delete(id)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this repository. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_list**
> InlineResponse2006 repositories_list(name=name, name__in=name__in, cursor=cursor)





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
name = 'name_example' # str |  (optional)
name__in = 'name__in_example' # str | Multiple values may be separated by commas. (optional)
cursor = 'cursor_example' # str | The pagination cursor value. (optional)

try:
    api_response = api_instance.repositories_list(name=name, name__in=name__in, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **name__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **cursor** | **str**| The pagination cursor value. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_partial_update**
> Repository repositories_partial_update(id, data)





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
id = 'id_example' # str | A UUID string identifying this repository.
data = swagger_client.Repository() # Repository | 

try:
    api_response = api_instance.repositories_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this repository. | 
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
> Repository repositories_read(id)





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
id = 'id_example' # str | A UUID string identifying this repository.

try:
    api_response = api_instance.repositories_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this repository. | 

### Return type

[**Repository**](Repository.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_update**
> Repository repositories_update(id, data)



Generates a Task to update a Repository

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
id = 'id_example' # str | A UUID string identifying this repository.
data = swagger_client.Repository() # Repository | 

try:
    api_response = api_instance.repositories_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this repository. | 
 **data** | [**Repository**](Repository.md)|  | 

### Return type

[**Repository**](Repository.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_versions_added_content**
> RepositoryVersion repositories_versions_added_content(repository_pk, number)



Display content added since the previous Repository Version.

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
repository_pk = 'repository_pk_example' # str | 
number = 56 # int | 

try:
    api_response = api_instance.repositories_versions_added_content(repository_pk, number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_versions_added_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_pk** | **str**|  | 
 **number** | **int**|  | 

### Return type

[**RepositoryVersion**](RepositoryVersion.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_versions_content**
> RepositoryVersion repositories_versions_content(repository_pk, number)





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
repository_pk = 'repository_pk_example' # str | 
number = 56 # int | 

try:
    api_response = api_instance.repositories_versions_content(repository_pk, number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_versions_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_pk** | **str**|  | 
 **number** | **int**|  | 

### Return type

[**RepositoryVersion**](RepositoryVersion.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_versions_create**
> RepositoryVersion repositories_versions_create(repository_pk, data)



Queues a task that creates a new RepositoryVersion by adding and removing content units

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
repository_pk = 'repository_pk_example' # str | 
data = swagger_client.RepositoryVersion() # RepositoryVersion | 

try:
    api_response = api_instance.repositories_versions_create(repository_pk, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_versions_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_pk** | **str**|  | 
 **data** | [**RepositoryVersion**](RepositoryVersion.md)|  | 

### Return type

[**RepositoryVersion**](RepositoryVersion.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_versions_delete**
> repositories_versions_delete(repository_pk, number)



Queues a task to handle deletion of a RepositoryVersion

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
repository_pk = 'repository_pk_example' # str | 
number = 56 # int | 

try:
    api_instance.repositories_versions_delete(repository_pk, number)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_versions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_pk** | **str**|  | 
 **number** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_versions_list**
> InlineResponse2007 repositories_versions_list(repository_pk, ordering=ordering, number=number, number__lt=number__lt, number__lte=number__lte, number__gt=number__gt, number__gte=number__gte, number__range=number__range, created__lt=created__lt, created__lte=created__lte, created__gt=created__gt, created__gte=created__gte, created__range=created__range, content=content, created=created, cursor=cursor)





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
repository_pk = 'repository_pk_example' # str | 
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
number = 8.14 # float |  (optional)
number__lt = 8.14 # float |  (optional)
number__lte = 8.14 # float |  (optional)
number__gt = 8.14 # float |  (optional)
number__gte = 8.14 # float |  (optional)
number__range = 8.14 # float | Multiple values may be separated by commas. (optional)
created__lt = 'created__lt_example' # str |  (optional)
created__lte = 'created__lte_example' # str |  (optional)
created__gt = 'created__gt_example' # str |  (optional)
created__gte = 'created__gte_example' # str |  (optional)
created__range = 'created__range_example' # str | Multiple values may be separated by commas. (optional)
content = 'content_example' # str | Content Unit referenced by HREF (optional)
created = 'created_example' # str |  (optional)
cursor = 'cursor_example' # str | The pagination cursor value. (optional)

try:
    api_response = api_instance.repositories_versions_list(repository_pk, ordering=ordering, number=number, number__lt=number__lt, number__lte=number__lte, number__gt=number__gt, number__gte=number__gte, number__range=number__range, created__lt=created__lt, created__lte=created__lte, created__gt=created__gt, created__gte=created__gte, created__range=created__range, content=content, created=created, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_versions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_pk** | **str**|  | 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **number** | **float**|  | [optional] 
 **number__lt** | **float**|  | [optional] 
 **number__lte** | **float**|  | [optional] 
 **number__gt** | **float**|  | [optional] 
 **number__gte** | **float**|  | [optional] 
 **number__range** | **float**| Multiple values may be separated by commas. | [optional] 
 **created__lt** | **str**|  | [optional] 
 **created__lte** | **str**|  | [optional] 
 **created__gt** | **str**|  | [optional] 
 **created__gte** | **str**|  | [optional] 
 **created__range** | **str**| Multiple values may be separated by commas. | [optional] 
 **content** | **str**| Content Unit referenced by HREF | [optional] 
 **created** | **str**|  | [optional] 
 **cursor** | **str**| The pagination cursor value. | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_versions_read**
> RepositoryVersion repositories_versions_read(repository_pk, number)





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
repository_pk = 'repository_pk_example' # str | 
number = 56 # int | 

try:
    api_response = api_instance.repositories_versions_read(repository_pk, number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_versions_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_pk** | **str**|  | 
 **number** | **int**|  | 

### Return type

[**RepositoryVersion**](RepositoryVersion.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_versions_removed_content**
> RepositoryVersion repositories_versions_removed_content(repository_pk, number)



Display content removed since the previous Repository Version.

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
repository_pk = 'repository_pk_example' # str | 
number = 56 # int | 

try:
    api_response = api_instance.repositories_versions_removed_content(repository_pk, number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoriesApi->repositories_versions_removed_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_pk** | **str**|  | 
 **number** | **int**|  | 

### Return type

[**RepositoryVersion**](RepositoryVersion.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

