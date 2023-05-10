from django.urls import  path
from .views import  about ,index , serch 



urlpatterns = [
    path('' , index , name='index' ),
    path('about/' , about , name='about' ),
    path('serch/' , serch , name='serch' ),

]