# MinimalTask

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**created** | **datetime** | Timestamp of creation. | [optional] 
**state** | **str** | The current state of the task. The possible values include: &#39;waiting&#39;, &#39;skipped&#39;, &#39;running&#39;, &#39;completed&#39;, &#39;failed&#39; and &#39;canceled&#39;. | [optional] 
**started_at** | **datetime** | Timestamp of the when this task started execution. | [optional] 
**finished_at** | **datetime** | Timestamp of the when this task stopped execution. | [optional] 
**worker** | **str** | The worker associated with this task. This field is empty if a worker is not yet assigned. | [optional] 
**parent** | **str** | The parent task that spawned this task. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


