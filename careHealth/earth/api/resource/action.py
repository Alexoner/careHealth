# -*- coding:utf-8 -*-
from ..exceptions import (
    ActionIntentException,
    OptionsRequiredException,
    ResourceTypeException,
)

from earth.action import RestJsonAction
from earth.base import get_api_id


class ResourceActionMetaclass(type):

    required_options = [
        'resource_name',
        'resource_type',
        'action_name',
        'action_intent',
        'action_ret_prefix',
    ]

    action_intent = [
        'create',
        'retrieve',
        'get',
        'update',
        'delete',
    ]

    resource_type = [
        'collection',
        'detail',
    ]

    def __new__(cls, name, bases, attrs):
        new_class = super(ResourceActionMetaclass, cls) \
            .__new__(cls, name, bases, attrs)

        if 'Options' not in new_class.__dict__:
            raise OptionsRequiredException(
                'Options required in ResourceAction'
            )

        options = getattr(new_class, 'Options')

        for opt_name in cls.required_options:
            if not hasattr(options, opt_name):
                raise OptionsRequiredException(
                    '%s required in Options' % opt_name
                )

        _opts = {}

        if name != 'ResourceAction':
            for action_intent in options.action_intent:
                if action_intent not in cls.action_intent:
                    raise ActionIntentException('Action intent invalid')

            if options.resource_type not in cls.resource_type:
                raise ResourceTypeException('Resource type invalid')

            if options.resource_type == 'collection':
                if hasattr(new_class, 'build_query_hook'):
                    if not hasattr(new_class, '_query_keys'):
                        raise OptionsRequiredException(
                            '_query_keys required when build_query_hook exists'
                        )

            api_id = get_api_id(
                'api.' + options.resource_name,
            )

            if api_id != -1:
                _opts['api_id'] = api_id
                new_class._ret_prefix = str(api_id) + \
                    str(options.action_ret_prefix)

        for opt_key in dir(options):
            if not opt_key.startswith('_'):
                opt_value = getattr(options, opt_key)
                _opts[opt_key] = opt_value

        new_class._opts = _opts

        return new_class


class ResourceAction(RestJsonAction):

    __metaclass__ = ResourceActionMetaclass

    def __init__(self, *args, **kwargs):
        super(ResourceAction, self).__init__(
            *args,
            **kwargs
        )

    def pre_process_hook(self, request, *args, **kwargs):
        if not super(ResourceAction, self).pre_process_hook(
            request,
            *args,
            **kwargs
        ):
            return False

        if self._opts['resource_type'] == 'detail':
            res_id_key = 'res_' + self._opts['resource_name'] + '_id'
            setattr(
                self,
                res_id_key,
                int(kwargs[res_id_key]),
            )

        if 'parent_resource' in self._opts:
            parent_resource = self._opts['parent_resource']
            res_id_key = 'res_' + parent_resource + '_id'
            setattr(
                self,
                res_id_key,
                int(kwargs[res_id_key]),
            )

        auth_hook = getattr(self, 'auth_hook', None)

        if auth_hook:
            if not auth_hook(self, request, *args, **kwargs):
                return False

        if self._opts['resource_type'] == 'collection':
            build_query_hook = getattr(self, 'build_query_hook', None)

            if build_query_hook and request.method.lower() == 'get':
                if not build_query_hook(self, request, *args, **kwargs):
                    return False

        return True

    @classmethod
    def opts(cls):
        return cls._opts

    @classmethod
    def resource_name(cls):
        return cls._opts['resource_name']

    @classmethod
    def resource_type(cls):
        return cls._opts['resource_type']

    @classmethod
    def action_name(cls):
        return cls._opts['action_name']

    @classmethod
    def action_intent(cls):
        return cls._opts['action_intent']

    class Options(object):
        resource_name = None
        resource_type = None
        action_name = None
        action_intent = None
        action_ret_prefix = None
