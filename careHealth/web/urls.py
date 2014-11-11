from django.conf.urls import url, include

urlpatterns = (
    url(r"^$", "web.site.views.index"),
    url(r"^site/", include("web.site.urls")),
    url(r"^user/", include("web.user.urls")),
)
