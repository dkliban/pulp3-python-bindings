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


class MinimalTask(object):
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
        'state': 'str',
        'started_at': 'datetime',
        'finished_at': 'datetime',
        'worker': 'str',
        'parent': 'str'
    }

    attribute_map = {
        'href': '_href',
        'created': 'created',
        'state': 'state',
        'started_at': 'started_at',
        'finished_at': 'finished_at',
        'worker': 'worker',
        'parent': 'parent'
    }

    def __init__(self, href=None, created=None, state=None, started_at=None, finished_at=None, worker=None, parent=None):  # noqa: E501
        """MinimalTask - a model defined in Swagger"""  # noqa: E501

        self._href = None
        self._created = None
        self._state = None
        self._started_at = None
        self._finished_at = None
        self._worker = None
        self._parent = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if created is not None:
            self.created = created
        if state is not None:
            self.state = state
        if started_at is not None:
            self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at
        if worker is not None:
            self.worker = worker
        if parent is not None:
            self.parent = parent

    @property
    def href(self):
        """Gets the href of this MinimalTask.  # noqa: E501


        :return: The href of this MinimalTask.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this MinimalTask.


        :param href: The href of this MinimalTask.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def created(self):
        """Gets the created of this MinimalTask.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The created of this MinimalTask.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this MinimalTask.

        Timestamp of creation.  # noqa: E501

        :param created: The created of this MinimalTask.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def state(self):
        """Gets the state of this MinimalTask.  # noqa: E501

        The current state of the task. The possible values include: 'waiting', 'skipped', 'running', 'completed', 'failed' and 'canceled'.  # noqa: E501

        :return: The state of this MinimalTask.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this MinimalTask.

        The current state of the task. The possible values include: 'waiting', 'skipped', 'running', 'completed', 'failed' and 'canceled'.  # noqa: E501

        :param state: The state of this MinimalTask.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def started_at(self):
        """Gets the started_at of this MinimalTask.  # noqa: E501

        Timestamp of the when this task started execution.  # noqa: E501

        :return: The started_at of this MinimalTask.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this MinimalTask.

        Timestamp of the when this task started execution.  # noqa: E501

        :param started_at: The started_at of this MinimalTask.  # noqa: E501
        :type: datetime
        """

        self._started_at = started_at

    @property
    def finished_at(self):
        """Gets the finished_at of this MinimalTask.  # noqa: E501

        Timestamp of the when this task stopped execution.  # noqa: E501

        :return: The finished_at of this MinimalTask.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this MinimalTask.

        Timestamp of the when this task stopped execution.  # noqa: E501

        :param finished_at: The finished_at of this MinimalTask.  # noqa: E501
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def worker(self):
        """Gets the worker of this MinimalTask.  # noqa: E501

        The worker associated with this task. This field is empty if a worker is not yet assigned.  # noqa: E501

        :return: The worker of this MinimalTask.  # noqa: E501
        :rtype: str
        """
        return self._worker

    @worker.setter
    def worker(self, worker):
        """Sets the worker of this MinimalTask.

        The worker associated with this task. This field is empty if a worker is not yet assigned.  # noqa: E501

        :param worker: The worker of this MinimalTask.  # noqa: E501
        :type: str
        """

        self._worker = worker

    @property
    def parent(self):
        """Gets the parent of this MinimalTask.  # noqa: E501

        The parent task that spawned this task.  # noqa: E501

        :return: The parent of this MinimalTask.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this MinimalTask.

        The parent task that spawned this task.  # noqa: E501

        :param parent: The parent of this MinimalTask.  # noqa: E501
        :type: str
        """

        self._parent = parent

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
        if not isinstance(other, MinimalTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
