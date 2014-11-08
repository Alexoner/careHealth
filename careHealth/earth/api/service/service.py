# -*- coding:utf-8 -*-
from django.conf.urls import url

from ..exceptions import (
    ActionTypeException
)

from .action import ServiceAction


class Service(object):

    def __init__(self, name):
        self._name = name
        self._actions = {}
        self._paths = {}
        self._url_patterns = []

    def add_action(self, action):
        if not issubclass(action, ServiceAction):
            raise ActionTypeException(
                'Action should be subclass of ServiceAction.'
            )

        action_name = action.action_name()
        self._actions[action_name] = action
        self._paths[action_name] = self._name + '/' \
            + action_name + '/'

        self._url_patterns.append(
            url(
                self._paths[action_name],
                action.as_view(),
            ),
        )

    @property
    def url_patterns(self):
        return self._url_patterns

    @property
    def paths(self):
        return self._paths

    @property
    def actions(self):
        return self._actions

    @property
    def name(self):
        return self._name
