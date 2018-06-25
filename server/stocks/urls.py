from django.conf.urls import url

from . import views

app_name = 'stocks'

urlpatterns = [
    url(r'^(?P<symbol>[-\w]+)/$', views.stock_timeseries_view, name='stock'),
    url('', views.stock_index_view, name='index'),
]
