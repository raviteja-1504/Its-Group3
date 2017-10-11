from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
	url(r'^',include('maps.urls')),#Here maps.urls means that in maps app we have urls.py to include that url. 
    url(r'^admin/', admin.site.urls),#Admin url
	
]
