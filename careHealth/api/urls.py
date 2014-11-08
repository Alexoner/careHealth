from django.conf.urls import patterns
from earth.api import Api

from api.example import ExampleResource

api_v1 = Api("v1")
api_v1.add_resource(ExampleResource())

urlpatterns = patterns(
    '',
    *api_v1.url_patterns
)
