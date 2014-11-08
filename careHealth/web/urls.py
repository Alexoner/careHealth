from django.conf.urls import url, include

urlpatterns = (
    url(r"^$", "web.index.views.index"),
    url(r"^index/", include("web.index.urls")),
)
