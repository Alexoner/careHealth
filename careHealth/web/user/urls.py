from django.conf.urls import url

urlpatterns = (
    url(r'^$', 'web.user.views.profile'),
    url(r'^register/$', 'web.user.views.register'),
    url(r'login/$', 'web.user.views.login'),
)
