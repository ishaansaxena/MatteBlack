from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<symbol>[-\w]+)/$', views.stock_default_view, name='profile_view'),
]
