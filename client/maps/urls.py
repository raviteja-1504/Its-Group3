from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^maps/farm/$', views.farm),#when the url is of the form for eg:https://10.0.3.23:7702/maps/farms it calls farm function in views
	url(r'^maps/house/$', views.house),#when the url is of the form for eg:https://10.0.3.23:7702/maps/house it calls house function in views
	url(r'^maps/well/$', views.well),#when the url is of the form for eg:https://10.0.3.23:7702/maps/well it calls well function in views
]
