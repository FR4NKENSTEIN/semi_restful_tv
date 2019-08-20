from django.conf.urls import url
from . import views
    
urlpatterns = [
    url(r'^$', views.root),
    url(r'^shows$', views.table),
    url(r'^shows/new', views.new),
    url(r'^shows/(?P<id>\d+)$', views.details),
    url(r'^shows/(?P<id>\d+)/edit$', views.edit),
    url(r'^create$', views.create),
    url(r'^update/(?P<id>\d+)$', views.update),
    url(r'^delete/(?P<id>\d+)$', views.delete),
]