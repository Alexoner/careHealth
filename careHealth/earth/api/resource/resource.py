# -*- coding:utf-8 -*-
from django.conf.urls import url

from ..exceptions import (
    ActionTypeException
)

from .action import ResourceAction


class Resource(object):

    def __init__(self, name):
        self._name = name
        self._actions = {}
        self._paths = {}
        self._url_patterns = []
        self._sub_resources = {}

        self._collection_path = '^' + self._name + '/$'
        self._detail_path = '^' + self._name + '/' + \
            '(?P<res_' + self._name + '_id>\d+)/$'

    def add_action(self, action):
        if not issubclass(action, ResourceAction):
            raise ActionTypeException(
                'Action should be subclass of ResourceAction'
            )

        resource_type = action.resource_type()
        action_intent = action.action_intent()

        for intent in action_intent:
            self._actions[intent] = action

        if resource_type == 'collection':
            self._url_patterns.append(
                url(
                    self._collection_path,
                    action.as_view(),
                ),
            )

            for intent in action_intent:
                self._paths[intent] = self._collection_path
        elif resource_type == 'detail':
            self._url_patterns.append(
                url(
                    self._detail_path,
                    action.as_view(),
                ),
            )

            for intent in action_intent:
                self._paths[intent] = self._detail_path

    def add_sub_resource(self, sub_res):
        self._sub_resources[sub_res.name] = sub_res

    def has_sub_res(self):
        return bool(self._sub_resources)

    @property
    def sub_res(self):
        return self._sub_resources

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
    def collection_path(self):
        return self._collection_path

    @property
    def detail_path(self):
        return self._detail_path

    @property
    def name(self):
        return self._name
