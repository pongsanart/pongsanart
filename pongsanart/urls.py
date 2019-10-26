from django.contrib import admin
from django.urls import path
from myapp import views as appview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',appview.home),
    path('index',appview.index),
    path('victims',appview.victims),


]
