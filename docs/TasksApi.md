# swagger_client.TasksApi

All URIs are relative to *http://localhost:8000/pulp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tasks_cancel**](TasksApi.md#tasks_cancel) | **POST** {href} | 
[**tasks_delete**](TasksApi.md#tasks_delete) | **DELETE** {href} | 
[**tasks_list**](TasksApi.md#tasks_list) | **GET** /tasks/ | 
[**tasks_read**](TasksApi.md#tasks_read) | **GET** {href} | 


# **tasks_cancel**
> Task tasks_cancel(href, data)





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
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
href = 'id_example' # str | A relative URI for the resource.
data = swagger_client.Task() # Task | 

try:
    api_response = api_instance.tasks_cancel(href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **href** | [**str**](.md)| A relative URI for the resource. | 
 **data** | [**Task**](Task.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_delete**
> tasks_delete(href)





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
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
href = 'id_example' # str | A relative URI for the resource.

try:
    api_instance.tasks_delete(href)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_delete: %s\n" % e)
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

# **tasks_list**
> InlineResponse2008 tasks_list(ordering=ordering, state=state, state__in=state__in, worker=worker, worker__in=worker__in, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, started_at__range=started_at__range, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, finished_at__range=finished_at__range, parent=parent, started_at=started_at, finished_at=finished_at, cursor=cursor)





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
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
state = 'state_example' # str |  (optional)
state__in = 'state__in_example' # str | Multiple values may be separated by commas. (optional)
worker = 'worker_example' # str | Foreign Key referenced by HREF (optional)
worker__in = 'worker__in_example' # str | Multiple values may be separated by commas. (optional)
started_at__lt = 'started_at__lt_example' # str |  (optional)
started_at__lte = 'started_at__lte_example' # str |  (optional)
started_at__gt = 'started_at__gt_example' # str |  (optional)
started_at__gte = 'started_at__gte_example' # str |  (optional)
started_at__range = 'started_at__range_example' # str | Multiple values may be separated by commas. (optional)
finished_at__lt = 'finished_at__lt_example' # str |  (optional)
finished_at__lte = 'finished_at__lte_example' # str |  (optional)
finished_at__gt = 'finished_at__gt_example' # str |  (optional)
finished_at__gte = 'finished_at__gte_example' # str |  (optional)
finished_at__range = 'finished_at__range_example' # str | Multiple values may be separated by commas. (optional)
parent = 'parent_example' # str | Foreign Key referenced by HREF (optional)
started_at = 'started_at_example' # str |  (optional)
finished_at = 'finished_at_example' # str |  (optional)
cursor = 'cursor_example' # str | The pagination cursor value. (optional)

try:
    api_response = api_instance.tasks_list(ordering=ordering, state=state, state__in=state__in, worker=worker, worker__in=worker__in, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, started_at__range=started_at__range, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, finished_at__range=finished_at__range, parent=parent, started_at=started_at, finished_at=finished_at, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **state** | **str**|  | [optional] 
 **state__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **worker** | **str**| Foreign Key referenced by HREF | [optional] 
 **worker__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **started_at__lt** | **str**|  | [optional] 
 **started_at__lte** | **str**|  | [optional] 
 **started_at__gt** | **str**|  | [optional] 
 **started_at__gte** | **str**|  | [optional] 
 **started_at__range** | **str**| Multiple values may be separated by commas. | [optional] 
 **finished_at__lt** | **str**|  | [optional] 
 **finished_at__lte** | **str**|  | [optional] 
 **finished_at__gt** | **str**|  | [optional] 
 **finished_at__gte** | **str**|  | [optional] 
 **finished_at__range** | **str**| Multiple values may be separated by commas. | [optional] 
 **parent** | **str**| Foreign Key referenced by HREF | [optional] 
 **started_at** | **str**|  | [optional] 
 **finished_at** | **str**|  | [optional] 
 **cursor** | **str**| The pagination cursor value. | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_read**
> Task tasks_read(href)





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
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
href = 'id_example' # str | A relative URI for the resource.

try:
    api_response = api_instance.tasks_read(href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **href** | [**str**](.md)| A relative URI for the resource. | 

### Return type

[**Task**](Task.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

