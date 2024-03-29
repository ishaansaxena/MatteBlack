from django.conf.urls import url

from . import views

app_name = 'stocks'

urlpatterns = [
    url(r'^(?P<symbol>[-\w]+)/track/$', views.track_stock_view, name='track'),
    url(r'^(?P<symbol>[-\w]+)/untrack/$', views.untrack_stock_view, name='untrack'),
    url(r'^(?P<symbol>[-\w]+)/t/(?P<format>[-\w]+)/$', views.stock_timeseries_view, name='timeseries'),
    url(r'^(?P<symbol>[-\w]+)/$', views.stock_timeseries_default, name='stock'),
    url('', views.stock_index_view, name='index'),
]

# TODO: In the future, we need to add support for different exchanges. Eg: "NSE:BPL"
# url(r'^(?P<symbol>[-\w]+[:]*[-\w]+)/track/$', views.track_stock_view, name='track'),
# url(r'^(?P<symbol>[-\w]+[:]*[-\w]+)/untrack/$', views.untrack_stock_view, name='untrack'),
# url(r'^(?P<symbol>[-\w]+[:]*[-\w]+)/t/(?P<format>[-\w]+)/$', views.stock_timeseries_view, name='timeseries'),
# url(r'^(?P<symbol>[-\w]+[:]*[-\w]+)/$', views.stock_timeseries_default, name='stock'),
