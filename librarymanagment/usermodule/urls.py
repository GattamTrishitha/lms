from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
path('viewbooks',views.viewbooks,name='viewbooks'),
path('feedback',views.feedback,name='feedback'),
]