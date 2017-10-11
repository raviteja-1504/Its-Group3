from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
#Here we define admin urls	
    url(r'^admin/', admin.site.urls),
	url(r'^', include('farms.urls')),#Here we include farms.urls meaning that in installed farms app go to urls
]
