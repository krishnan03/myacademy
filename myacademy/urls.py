
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('userProfile/',include('userPage.urls')),
    url('home/',include('home.urls')),
]
