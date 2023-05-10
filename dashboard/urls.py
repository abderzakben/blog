from django.urls import path
from . import views
from django.contrib.auth  import views as auth_views 

urlpatterns = [
   ###############################
   path('dashboard/', views.home ,name='home' ),
   path('notes/', views.notes , name='notes' ),
   path('delete_note/<int:pk>' , views.delete_note , name='delete-note'),
   path('note_detail/<int:pk>', views.NotesDetailVies.as_view() , name='detail-note'),
   ###############################
   path('homework/', views.homework , name='homework' ),
   path('update_homework/<int:pk>', views.update_homework , name='update-homework' ),
   path('delete_homework/<int:pk>', views.delete_homework , name='delete-homework' ),
   ###############################
   path('youtube/', views.youtube , name='youtube' ),
   ###############################
   path('todo/', views.todo , name='todo' ),
   path('update_todo/<int:pk>', views.update_todo , name='update-todo' ),
   path('delete_todo/<int:pk>', views.delete_todo , name='delete-todo' ),
   ###############################
   path('books/', views.books , name='books'),
   #########################################
   path('dictionary/', views.dictionary , name='dictionary'),
   #########################################
   path('wiki/', views.wiki, name='wiki'),
   #########################################
   path('conversion/', views.conversion, name='conversion'),
   #########################################

   #path('register/', views.register, name='register_app'),
   #path('login/', auth_views.LoginView.as_view(template_name ="dashboard/login.html"), name='login'),
   #path('logout/', auth_views.LogoutView.as_view(template_name ="dashboard/logout.html"), name='logout'),
   #path('profile/', views.profile, name='profile'),
]