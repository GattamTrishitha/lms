from django.contrib import admin
from django.urls import path, include
from .import views
app_name='librarymodule'
urlpatterns = [
   path('librarybooks',views.librarybooks,name='librarybooks'),
   path('add_book_details',views.add_Book_Details,name='add_book_details'),
   path('view',views.view_book_details,name='view_book_details'),
]