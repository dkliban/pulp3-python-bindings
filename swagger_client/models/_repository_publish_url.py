# coding: utf-8

"""
    Pulp3 API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RepositoryPublishURL(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'repository': 'str',
        'repository_version': 'str'
    }

    attribute_map = {
        'repository': 'repository',
        'repository_version': 'repository_version'
    }

    def __init__(self, repository=None, repository_version=None):  # noqa: E501
        """RepositoryPublishURL - a model defined in Swagger"""  # noqa: E501

        self._repository = None
        self._repository_version = None
        self.discriminator = None

        if repository is not None:
            self.repository = repository
        if repository_version is not None:
            self.repository_version = repository_version

    @property
    def repository(self):
        """Gets the repository of this RepositoryPublishURL.  # noqa: E501

        A URI of the repository to be synchronized.  # noqa: E501

        :return: The repository of this RepositoryPublishURL.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this RepositoryPublishURL.

        A URI of the repository to be synchronized.  # noqa: E501

        :param repository: The repository of this RepositoryPublishURL.  # noqa: E501
        :type: str
        """

        self._repository = repository

    @property
    def repository_version(self):
        """Gets the repository_version of this RepositoryPublishURL.  # noqa: E501

        A URI of the repository version to be published.  # noqa: E501

        :return: The repository_version of this RepositoryPublishURL.  # noqa: E501
        :rtype: str
        """
        return self._repository_version

    @repository_version.setter
    def repository_version(self, repository_version):
        """Sets the repository_version of this RepositoryPublishURL.

        A URI of the repository version to be published.  # noqa: E501

        :param repository_version: The repository_version of this RepositoryPublishURL.  # noqa: E501
        :type: str
        """

        self._repository_version = repository_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RepositoryPublishURL):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
