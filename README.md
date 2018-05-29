# swagger-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v3
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'
# create an instance of the API class
api_instance = swagger_client.ArtifactsApi()
data = swagger_client.Artifact() # Artifact | 

try:
    api_response = api_instance.artifacts_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->artifacts_create: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8000/pulp/api/v3*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ArtifactsApi* | [**artifacts_create**](docs/ArtifactsApi.md#artifacts_create) | **POST** /artifacts/ | 
*ArtifactsApi* | [**artifacts_delete**](docs/ArtifactsApi.md#artifacts_delete) | **DELETE** {href} | 
*ArtifactsApi* | [**artifacts_list**](docs/ArtifactsApi.md#artifacts_list) | **GET** /artifacts/ | 
*ArtifactsApi* | [**artifacts_read**](docs/ArtifactsApi.md#artifacts_read) | **GET** {href} | 
*ContentApi* | [**content_file_create**](docs/ContentApi.md#content_file_create) | **POST** /content/file/ | 
*ContentApi* | [**content_file_list**](docs/ContentApi.md#content_file_list) | **GET** /content/file/ | 
*ContentApi* | [**content_file_read**](docs/ContentApi.md#content_file_read) | **GET** {href} | 
*DistributionsApi* | [**distributions_create**](docs/DistributionsApi.md#distributions_create) | **POST** /distributions/ | 
*DistributionsApi* | [**distributions_delete**](docs/DistributionsApi.md#distributions_delete) | **DELETE** {href} | 
*DistributionsApi* | [**distributions_list**](docs/DistributionsApi.md#distributions_list) | **GET** /distributions/ | 
*DistributionsApi* | [**distributions_partial_update**](docs/DistributionsApi.md#distributions_partial_update) | **PATCH** {href} | 
*DistributionsApi* | [**distributions_read**](docs/DistributionsApi.md#distributions_read) | **GET** {href} | 
*DistributionsApi* | [**distributions_update**](docs/DistributionsApi.md#distributions_update) | **PUT** {href} | 
*OrphansApi* | [**orphans_delete**](docs/OrphansApi.md#orphans_delete) | **DELETE** /orphans/ | 
*PublicationsApi* | [**publications_delete**](docs/PublicationsApi.md#publications_delete) | **DELETE** {href} | 
*PublicationsApi* | [**publications_list**](docs/PublicationsApi.md#publications_list) | **GET** /publications/ | 
*PublicationsApi* | [**publications_read**](docs/PublicationsApi.md#publications_read) | **GET** {href} | 
*PublishersApi* | [**publishers_file_create**](docs/PublishersApi.md#publishers_file_create) | **POST** /publishers/file/ | 
*PublishersApi* | [**publishers_file_delete**](docs/PublishersApi.md#publishers_file_delete) | **DELETE** {href} | 
*PublishersApi* | [**publishers_file_list**](docs/PublishersApi.md#publishers_file_list) | **GET** /publishers/file/ | 
*PublishersApi* | [**publishers_file_partial_update**](docs/PublishersApi.md#publishers_file_partial_update) | **PATCH** {href} | 
*PublishersApi* | [**publishers_file_publish**](docs/PublishersApi.md#publishers_file_publish) | **POST** {href} | 
*PublishersApi* | [**publishers_file_read**](docs/PublishersApi.md#publishers_file_read) | **GET** {href} | 
*PublishersApi* | [**publishers_file_update**](docs/PublishersApi.md#publishers_file_update) | **PUT** {href} | 
*RemotesApi* | [**remotes_file_create**](docs/RemotesApi.md#remotes_file_create) | **POST** /remotes/file/ | 
*RemotesApi* | [**remotes_file_delete**](docs/RemotesApi.md#remotes_file_delete) | **DELETE** {href} | 
*RemotesApi* | [**remotes_file_list**](docs/RemotesApi.md#remotes_file_list) | **GET** /remotes/file/ | 
*RemotesApi* | [**remotes_file_partial_update**](docs/RemotesApi.md#remotes_file_partial_update) | **PATCH** {href} | 
*RemotesApi* | [**remotes_file_read**](docs/RemotesApi.md#remotes_file_read) | **GET** {href} | 
*RemotesApi* | [**remotes_file_sync**](docs/RemotesApi.md#remotes_file_sync) | **POST** {href} | 
*RemotesApi* | [**remotes_file_update**](docs/RemotesApi.md#remotes_file_update) | **PUT** {href} | 
*RepositoriesApi* | [**repositories_create**](docs/RepositoriesApi.md#repositories_create) | **POST** /repositories/ | 
*RepositoriesApi* | [**repositories_delete**](docs/RepositoriesApi.md#repositories_delete) | **DELETE** {href} | 
*RepositoriesApi* | [**repositories_list**](docs/RepositoriesApi.md#repositories_list) | **GET** /repositories/ | 
*RepositoriesApi* | [**repositories_partial_update**](docs/RepositoriesApi.md#repositories_partial_update) | **PATCH** {href} | 
*RepositoriesApi* | [**repositories_read**](docs/RepositoriesApi.md#repositories_read) | **GET** {href} | 
*RepositoriesApi* | [**repositories_update**](docs/RepositoriesApi.md#repositories_update) | **PUT** {href} | 
*RepositoriesApi* | [**repositories_versions_added_content**](docs/RepositoriesApi.md#repositories_versions_added_content) | **GET** {href} | 
*RepositoriesApi* | [**repositories_versions_content**](docs/RepositoriesApi.md#repositories_versions_content) | **GET** {href} | 
*RepositoriesApi* | [**repositories_versions_create**](docs/RepositoriesApi.md#repositories_versions_create) | **POST** {href} | 
*RepositoriesApi* | [**repositories_versions_delete**](docs/RepositoriesApi.md#repositories_versions_delete) | **DELETE** {href} | 
*RepositoriesApi* | [**repositories_versions_list**](docs/RepositoriesApi.md#repositories_versions_list) | **GET** {href} | 
*RepositoriesApi* | [**repositories_versions_read**](docs/RepositoriesApi.md#repositories_versions_read) | **GET** {href} | 
*RepositoriesApi* | [**repositories_versions_removed_content**](docs/RepositoriesApi.md#repositories_versions_removed_content) | **GET** {href} | 
*StatusApi* | [**status_list**](docs/StatusApi.md#status_list) | **GET** /status/ | 
*TasksApi* | [**tasks_cancel**](docs/TasksApi.md#tasks_cancel) | **POST** {href} | 
*TasksApi* | [**tasks_delete**](docs/TasksApi.md#tasks_delete) | **DELETE** {href} | 
*TasksApi* | [**tasks_list**](docs/TasksApi.md#tasks_list) | **GET** /tasks/ | 
*TasksApi* | [**tasks_read**](docs/TasksApi.md#tasks_read) | **GET** {href} | 
*UsersApi* | [**users_create**](docs/UsersApi.md#users_create) | **POST** /users/ | 
*UsersApi* | [**users_delete**](docs/UsersApi.md#users_delete) | **DELETE** {href} | 
*UsersApi* | [**users_list**](docs/UsersApi.md#users_list) | **GET** /users/ | 
*UsersApi* | [**users_partial_update**](docs/UsersApi.md#users_partial_update) | **PATCH** {href} | 
*UsersApi* | [**users_read**](docs/UsersApi.md#users_read) | **GET** {href} | 
*UsersApi* | [**users_update**](docs/UsersApi.md#users_update) | **PUT** {href} | 
*WorkersApi* | [**workers_list**](docs/WorkersApi.md#workers_list) | **GET** /workers/ | 
*WorkersApi* | [**workers_read**](docs/WorkersApi.md#workers_read) | **GET** {href} | 


## Documentation For Models

 - [Artifact](docs/Artifact.md)
 - [CreatedResource](docs/CreatedResource.md)
 - [Distribution](docs/Distribution.md)
 - [FileContent](docs/FileContent.md)
 - [FilePublisher](docs/FilePublisher.md)
 - [FileRemote](docs/FileRemote.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [MinimalTask](docs/MinimalTask.md)
 - [ProgressReport](docs/ProgressReport.md)
 - [Publication](docs/Publication.md)
 - [Repository](docs/Repository.md)
 - [RepositoryPublishURL](docs/RepositoryPublishURL.md)
 - [RepositorySyncURL](docs/RepositorySyncURL.md)
 - [RepositoryVersion](docs/RepositoryVersion.md)
 - [Task](docs/Task.md)
 - [User](docs/User.md)
 - [Worker](docs/Worker.md)


## Documentation For Authorization


## basic

- **Type**: HTTP basic authentication


## Author



