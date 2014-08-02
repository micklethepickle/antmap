from django.conf.urls import patterns, url
from antmap import views

urlpatterns = patterns('',
	url(r'^antlist/$', views.ant_list, name='ant_list'),
)
