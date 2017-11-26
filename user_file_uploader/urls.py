from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^profile/(?P<username>[a-zA-Z0-9]+)$', views.get_user_profile_view, name='get_user_profile'),
    url(r'^login/$', auth_views.login, {'template_name' : 'login.html'}, name='login'),
]