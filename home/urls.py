from django.conf.urls import url
from django.contrib import admin
from userPage import views

app_name='home'
urlpatterns = [
    url('', views.index, name='home'),
]

