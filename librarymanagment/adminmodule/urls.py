from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
   path('',views.projecthomepage, name='projecthomepage'),
   path('libraryhomepage',views.libraryhomepage, name='libraryhomepage'),
   path('userhomepage',views.userhomepage, name='userhomepage'),
   path('login',views.login, name='login'),
   path('login1',views.login1,name='login1'),
   path('logout',views.logout_view,name='logout'),
   path('signup',views.signup,name='signup'),
   path('signup1', views.signup1, name='signup1'),

]