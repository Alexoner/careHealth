from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'careHealth.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'web.index.views.index'),
                       url(r'web/', include('web.urls')),
                       url(r'api/', include('api.urls')),
                       url(r'accounts/', include(
                           'accounts.urls', namespace='accounts')),
                       )
