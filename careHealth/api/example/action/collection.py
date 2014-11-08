from earth.api import ResourceAction

from ..models import Example

class ExampleCollection(ResourceAction):
    def get(self, request, *args, **kwargs):
        return True

    class Options(object):
        resource_name = 'example'
        resource_type = 'collection'
        action_name = 'example_collection'
        action_intent = ['create', 'retrieve']
        action_ret_prefix = 1
