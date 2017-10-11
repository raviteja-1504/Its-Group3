from django.conf.urls import url

from farms import views


urlpatterns = [

	url(r'^farms/(?P<name>[a-z]+)/$', views.data)#Here url pattern is  defined as something/farms/name where name can be houselist,personinfo...etc eg:https://10.0.3.23:7702/farms/houselist(name) and we call views having function data as views.data
]


