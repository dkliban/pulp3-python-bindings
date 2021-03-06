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


class FileContent(object):
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
        'type': 'str',
        'relative_path': 'str',
        'artifact': 'str'
    }

    attribute_map = {
        'href': '_href',
        'type': 'type',
        'relative_path': 'relative_path',
        'artifact': 'artifact'
    }

    def __init__(self, href=None, type=None, relative_path=None, artifact=None):  # noqa: E501
        """FileContent - a model defined in Swagger"""  # noqa: E501

        self._href = None
        self._type = None
        self._relative_path = None
        self._artifact = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if type is not None:
            self.type = type
        self.relative_path = relative_path
        self.artifact = artifact

    @property
    def href(self):
        """Gets the href of this FileContent.  # noqa: E501


        :return: The href of this FileContent.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this FileContent.


        :param href: The href of this FileContent.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def type(self):
        """Gets the type of this FileContent.  # noqa: E501


        :return: The type of this FileContent.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FileContent.


        :param type: The type of this FileContent.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def relative_path(self):
        """Gets the relative_path of this FileContent.  # noqa: E501

        Relative location of the file within the repository  # noqa: E501

        :return: The relative_path of this FileContent.  # noqa: E501
        :rtype: str
        """
        return self._relative_path

    @relative_path.setter
    def relative_path(self, relative_path):
        """Sets the relative_path of this FileContent.

        Relative location of the file within the repository  # noqa: E501

        :param relative_path: The relative_path of this FileContent.  # noqa: E501
        :type: str
        """
        if relative_path is None:
            raise ValueError("Invalid value for `relative_path`, must not be `None`")  # noqa: E501

        self._relative_path = relative_path

    @property
    def artifact(self):
        """Gets the artifact of this FileContent.  # noqa: E501

        Artifact file representing the physical content  # noqa: E501

        :return: The artifact of this FileContent.  # noqa: E501
        :rtype: str
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact):
        """Sets the artifact of this FileContent.

        Artifact file representing the physical content  # noqa: E501

        :param artifact: The artifact of this FileContent.  # noqa: E501
        :type: str
        """
        if artifact is None:
            raise ValueError("Invalid value for `artifact`, must not be `None`")  # noqa: E501

        self._artifact = artifact

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
        if not isinstance(other, FileContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
