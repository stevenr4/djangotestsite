from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register_user/$', views.register_user, name='register_user'),
    url(r'^confirmation/$', views.confirmation, name='confirmation'),
    url(r'^$', views.index, name='index'),
]