from earth.api import ResourceAction

from ..models import Example

class ExampleDetail(ResourceAction):
    def get(self, request, *args, **kwargs):
        return True

    class Options(object):
        resource_name = "example"
        resource_type = "detail"
        action_name = "example_detail"
        action_intent = ['get', 'update', 'delete']
        action_ret_prefix = 2
