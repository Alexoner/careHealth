# -*- coding:utf-8 -*-
from django.conf.urls import url, include


class Api(object):

    def __init__(self, name):
        self._name = name
        self._services = {}
        self._resources = {}
        self._url_patterns = []
        self._api_path_prefix = r'api/(?P<api_name>%s)/' % name

    def add_service(self, service):
        self._services[service.name] = service
        self._url_patterns.append(
            url(
                self._api_path_prefix,
                include(service.url_patterns),
            ),
        )

    def add_resource(self, resource):
        self._resources[resource.name] = resource
        self._url_patterns.append(
            url(
                self._api_path_prefix,
                include(resource.url_patterns),
            ),
        )

        if resource.has_sub_res():
            for sub_res in resource.sub_res():
                sub_res_prefix = self._api_path_prefix + \
                    resource.detail_path

                self._url_patterns.append(
                    url(
                        sub_res_prefix,
                        sub_res.url_patterns,
                    ),
                )

    @property
    def url_patterns(self):
        return self._url_patterns
