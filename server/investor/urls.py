from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'investor'

urlpatterns = [
    url(
        r'^login/$',
        auth_views.login,
        {
            'template_name': 'investor/login.html',
        },
        name='login'
    ),
    url(
        r'^logout/$',
        auth_views.logout,
        {
            'next_page': '/',
        },
        name='logout'
    ),
]
