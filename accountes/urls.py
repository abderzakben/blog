from django.urls import  path
from .views import singup_page  , login_page , logout ,profile 



urlpatterns = [
    path('singup/', singup_page , name='singup' ),
    path('login/', login_page , name='login' ),
    path('profile/', profile , name='profile' ),
    path('logout/', logout    , name='logout' ),
    


]