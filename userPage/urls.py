from django.conf.urls import url
from django.contrib import admin
from userPage import views

app_name='userPage'
urlpatterns = [
    url('', views.index, name='userMain'),

]

