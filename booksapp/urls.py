from django.urls import  path
from .views import books , all_books , category_detail , book_detail



urlpatterns = [


    path('home/',  books , name='bookss' ),
    path('all_books/', all_books , name='all_bookss' ),
    path('genre/<str:slug>',category_detail , name='category_detail' ),
    path('detail/<str:slug>', book_detail , name='book_detail' ),

    


]