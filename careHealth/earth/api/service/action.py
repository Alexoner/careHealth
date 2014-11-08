# -*- coding:utf-8 -*-
from ..exceptions import OptionsRequiredException

from earth.action import RestJsonAction
from earth.base import get_api_id


class ServiceActionMetaclass(type):

    required_options = [
        'service_name',
        'action_name',
        'action_ret_prefix',
    ]

    def __new__(cls, name, bases, attrs):
        new_class = super(ServiceActionMetaclass, cls) \
            .__new__(cls, name, bases, attrs)

        if 'Options' not in new_class.__dict__:
            raise OptionsRequiredException(
                'Options required in ServiceAction'
            )

        options = getattr(new_class, 'Options')

        for opt_name in cls.required_options:
            if not hasattr(options, opt_name):
                raise OptionsRequiredException(
                    '%s required in Options.' % opt_name
                )

        _opts = {}

        if name != 'ServiceAction':
            api_id = get_api_id(
                'serv.' + options.service_name,
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


class ServiceAction(RestJsonAction):

    __metaclass__ = ServiceActionMetaclass

    def pre_process_hook(self, request, *args, **kwargs):
        if not super(ServiceAction, self).pre_process_hook(
            request,
            *args,
            **kwargs
        ):
            return False

        auth_hook = getattr(self, 'auth_hook', None)

        if auth_hook:
            if not auth_hook(self, request, *args, **kwargs):
                return False

        return True

    @classmethod
    def opts(cls):
        return cls._opts

    @classmethod
    def service_name(cls):
        return cls._opts['service_name']

    @classmethod
    def action_name(cls):
        return cls._opts['action_name']

    class Options(object):
        service_name = None
        action_name = None
        action_ret_prefix = None
