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


class Publication(object):
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
        'href': 'str',
        'created': 'datetime',
        'publisher': 'str',
        'distributions': 'list[str]',
        'repository_version': 'str'
    }

    attribute_map = {
        'href': '_href',
        'created': 'created',
        'publisher': 'publisher',
        'distributions': 'distributions',
        'repository_version': 'repository_version'
    }

    def __init__(self, href=None, created=None, publisher=None, distributions=None, repository_version=None):  # noqa: E501
        """Publication - a model defined in Swagger"""  # noqa: E501

        self._href = None
        self._created = None
        self._publisher = None
        self._distributions = None
        self._repository_version = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if created is not None:
            self.created = created
        self.publisher = publisher
        if distributions is not None:
            self.distributions = distributions
        if repository_version is not None:
            self.repository_version = repository_version

    @property
    def href(self):
        """Gets the href of this Publication.  # noqa: E501


        :return: The href of this Publication.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Publication.


        :param href: The href of this Publication.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def created(self):
        """Gets the created of this Publication.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The created of this Publication.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Publication.

        Timestamp of creation.  # noqa: E501

        :param created: The created of this Publication.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def publisher(self):
        """Gets the publisher of this Publication.  # noqa: E501

        The publisher that created this publication.  # noqa: E501

        :return: The publisher of this Publication.  # noqa: E501
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this Publication.

        The publisher that created this publication.  # noqa: E501

        :param publisher: The publisher of this Publication.  # noqa: E501
        :type: str
        """
        if publisher is None:
            raise ValueError("Invalid value for `publisher`, must not be `None`")  # noqa: E501

        self._publisher = publisher

    @property
    def distributions(self):
        """Gets the distributions of this Publication.  # noqa: E501

        This publication is currently being served asdefined by these distributions.  # noqa: E501

        :return: The distributions of this Publication.  # noqa: E501
        :rtype: list[str]
        """
        return self._distributions

    @distributions.setter
    def distributions(self, distributions):
        """Sets the distributions of this Publication.

        This publication is currently being served asdefined by these distributions.  # noqa: E501

        :param distributions: The distributions of this Publication.  # noqa: E501
        :type: list[str]
        """

        self._distributions = distributions

    @property
    def repository_version(self):
        """Gets the repository_version of this Publication.  # noqa: E501


        :return: The repository_version of this Publication.  # noqa: E501
        :rtype: str
        """
        return self._repository_version

    @repository_version.setter
    def repository_version(self, repository_version):
        """Sets the repository_version of this Publication.


        :param repository_version: The repository_version of this Publication.  # noqa: E501
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
        if not isinstance(other, Publication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
