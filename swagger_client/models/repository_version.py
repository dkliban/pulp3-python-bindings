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


class RepositoryVersion(object):
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
        'id': 'int',
        'href': 'str',
        'created': 'datetime',
        'content_href': 'str',
        'added_href': 'str',
        'removed_href': 'str',
        'number': 'int',
        'content_summary': 'dict(str, str)',
        'add_content_units': 'list[str]',
        'remove_content_units': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'href': '_href',
        'created': 'created',
        'content_href': '_content_href',
        'added_href': '_added_href',
        'removed_href': '_removed_href',
        'number': 'number',
        'content_summary': 'content_summary',
        'add_content_units': 'add_content_units',
        'remove_content_units': 'remove_content_units'
    }

    def __init__(self, id=None, href=None, created=None, content_href=None, added_href=None, removed_href=None, number=None, content_summary=None, add_content_units=None, remove_content_units=None):  # noqa: E501
        """RepositoryVersion - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._href = None
        self._created = None
        self._content_href = None
        self._added_href = None
        self._removed_href = None
        self._number = None
        self._content_summary = None
        self._add_content_units = None
        self._remove_content_units = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if created is not None:
            self.created = created
        if content_href is not None:
            self.content_href = content_href
        if added_href is not None:
            self.added_href = added_href
        if removed_href is not None:
            self.removed_href = removed_href
        if number is not None:
            self.number = number
        if content_summary is not None:
            self.content_summary = content_summary
        self.add_content_units = add_content_units
        self.remove_content_units = remove_content_units

    @property
    def id(self):
        """Gets the id of this RepositoryVersion.  # noqa: E501


        :return: The id of this RepositoryVersion.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RepositoryVersion.


        :param id: The id of this RepositoryVersion.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this RepositoryVersion.  # noqa: E501


        :return: The href of this RepositoryVersion.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this RepositoryVersion.


        :param href: The href of this RepositoryVersion.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def created(self):
        """Gets the created of this RepositoryVersion.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The created of this RepositoryVersion.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this RepositoryVersion.

        Timestamp of creation.  # noqa: E501

        :param created: The created of this RepositoryVersion.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def content_href(self):
        """Gets the content_href of this RepositoryVersion.  # noqa: E501


        :return: The content_href of this RepositoryVersion.  # noqa: E501
        :rtype: str
        """
        return self._content_href

    @content_href.setter
    def content_href(self, content_href):
        """Sets the content_href of this RepositoryVersion.


        :param content_href: The content_href of this RepositoryVersion.  # noqa: E501
        :type: str
        """

        self._content_href = content_href

    @property
    def added_href(self):
        """Gets the added_href of this RepositoryVersion.  # noqa: E501


        :return: The added_href of this RepositoryVersion.  # noqa: E501
        :rtype: str
        """
        return self._added_href

    @added_href.setter
    def added_href(self, added_href):
        """Sets the added_href of this RepositoryVersion.


        :param added_href: The added_href of this RepositoryVersion.  # noqa: E501
        :type: str
        """

        self._added_href = added_href

    @property
    def removed_href(self):
        """Gets the removed_href of this RepositoryVersion.  # noqa: E501


        :return: The removed_href of this RepositoryVersion.  # noqa: E501
        :rtype: str
        """
        return self._removed_href

    @removed_href.setter
    def removed_href(self, removed_href):
        """Sets the removed_href of this RepositoryVersion.


        :param removed_href: The removed_href of this RepositoryVersion.  # noqa: E501
        :type: str
        """

        self._removed_href = removed_href

    @property
    def number(self):
        """Gets the number of this RepositoryVersion.  # noqa: E501


        :return: The number of this RepositoryVersion.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this RepositoryVersion.


        :param number: The number of this RepositoryVersion.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def content_summary(self):
        """Gets the content_summary of this RepositoryVersion.  # noqa: E501

        A list of counts of each type of content in this version.  # noqa: E501

        :return: The content_summary of this RepositoryVersion.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._content_summary

    @content_summary.setter
    def content_summary(self, content_summary):
        """Sets the content_summary of this RepositoryVersion.

        A list of counts of each type of content in this version.  # noqa: E501

        :param content_summary: The content_summary of this RepositoryVersion.  # noqa: E501
        :type: dict(str, str)
        """

        self._content_summary = content_summary

    @property
    def add_content_units(self):
        """Gets the add_content_units of this RepositoryVersion.  # noqa: E501

        A list of content units to add to a new repository version  # noqa: E501

        :return: The add_content_units of this RepositoryVersion.  # noqa: E501
        :rtype: list[str]
        """
        return self._add_content_units

    @add_content_units.setter
    def add_content_units(self, add_content_units):
        """Sets the add_content_units of this RepositoryVersion.

        A list of content units to add to a new repository version  # noqa: E501

        :param add_content_units: The add_content_units of this RepositoryVersion.  # noqa: E501
        :type: list[str]
        """
        if add_content_units is None:
            raise ValueError("Invalid value for `add_content_units`, must not be `None`")  # noqa: E501

        self._add_content_units = add_content_units

    @property
    def remove_content_units(self):
        """Gets the remove_content_units of this RepositoryVersion.  # noqa: E501

        A list of content units to remove from the latest repository version  # noqa: E501

        :return: The remove_content_units of this RepositoryVersion.  # noqa: E501
        :rtype: list[str]
        """
        return self._remove_content_units

    @remove_content_units.setter
    def remove_content_units(self, remove_content_units):
        """Sets the remove_content_units of this RepositoryVersion.

        A list of content units to remove from the latest repository version  # noqa: E501

        :param remove_content_units: The remove_content_units of this RepositoryVersion.  # noqa: E501
        :type: list[str]
        """
        if remove_content_units is None:
            raise ValueError("Invalid value for `remove_content_units`, must not be `None`")  # noqa: E501

        self._remove_content_units = remove_content_units

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
        if not isinstance(other, RepositoryVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
