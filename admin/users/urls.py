from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.UserFormView.as_view(),
        name='search'),
    url(r'^id-(?P<guid>[a-z0-9]+)/$', views.UserView.as_view(),
        name='user'),
    url(r'^id-(?P<guid>[a-z0-9]+)/two-factor/disable/$', views.remove_2_factor,
        name='remove2factor'),
]
