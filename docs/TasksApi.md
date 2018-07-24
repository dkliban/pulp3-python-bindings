# swagger_client.TasksApi

All URIs are relative to *http://localhost:8000/pulp/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tasks_cancel**](TasksApi.md#tasks_cancel) | **POST** /{task_href}/cancel/ | 
[**tasks_delete**](TasksApi.md#tasks_delete) | **DELETE** /{task_href}/ | 
[**tasks_list**](TasksApi.md#tasks_list) | **GET** /tasks/ | 
[**tasks_read**](TasksApi.md#tasks_read) | **GET** /{task_href}/ | 


# **tasks_cancel**
> Task tasks_cancel(task_href, data)





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
task_href = 'task_href_example' # str | URI of Task. e.g.: /tasks/1/
data = swagger_client.Task() # Task | 

try:
    api_response = api_instance.tasks_cancel(task_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_href** | **str**| URI of Task. e.g.: /tasks/1/ | 
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
> tasks_delete(task_href)





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
task_href = 'task_href_example' # str | URI of Task. e.g.: /tasks/1/

try:
    api_instance.tasks_delete(task_href)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_href** | **str**| URI of Task. e.g.: /tasks/1/ | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_list**
> InlineResponse2007 tasks_list(ordering=ordering, state=state, state__in=state__in, worker=worker, worker__in=worker__in, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, started_at__range=started_at__range, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, finished_at__range=finished_at__range, parent=parent, started_at=started_at, finished_at=finished_at, cursor=cursor, page_size=page_size)





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
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.tasks_list(ordering=ordering, state=state, state__in=state__in, worker=worker, worker__in=worker__in, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, started_at__range=started_at__range, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, finished_at__range=finished_at__range, parent=parent, started_at=started_at, finished_at=finished_at, cursor=cursor, page_size=page_size)
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
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_read**
> Task tasks_read(task_href)





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
task_href = 'task_href_example' # str | URI of Task. e.g.: /tasks/1/

try:
    api_response = api_instance.tasks_read(task_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_href** | **str**| URI of Task. e.g.: /tasks/1/ | 

### Return type

[**Task**](Task.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

