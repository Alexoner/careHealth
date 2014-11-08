from earth.api import Resource

from ..action import ExampleCollection
from ..action import ExampleDetail

class ExampleResource(Resource):

    def __init__(self):
        super(ExampleResource, self).__init__('example')
        self.add_action(ExampleCollection,)
        self.add_action(ExampleDetail,)

