from django.conf.urls import url

from . import views

app_name = 'stocks'

urlpatterns = [
    url('', views.stock_index_view, name='index'),
    url(r'^(?P<symbol>[-\w]+)/$', views.stock_default_view, name='stock'),
]
