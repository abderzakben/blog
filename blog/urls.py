from unicodedata import name
from django.urls import  path
from .views import home ,tags_list ,PostDetail ,tags_list ,TagDetail,TagCreate , PostCreate  , TagUpdate , PostUpdate , TagDelete , PostDelete , AddCommentbView   

urlpatterns = [

    #################### Url Post Cours #################
    path('blog/' , home , name='home-blog' ),
    path('post/create', PostCreate.as_view(), name='post_create'),
    path('post/<str:slug>/' , PostDetail.as_view() , name = 'post_detail_url'),
    path('post/<str:slug>/update/', PostUpdate.as_view() , name='post_update_url' ),
    path('post/<str:slug>/delete/' , PostDelete.as_view(), name='post_delete_url'),
    path('post/<int:pk>/comment' , AddCommentbView.as_view() , name='add_commenter'),

    #################### Url Post Models  #################
    path('tags/' , tags_list , name='tags_list'),
    path('tag/create' , TagCreate.as_view() , name='tag_creat'),
    path('tag/<str:slug>/' , TagDetail.as_view() , name='tag_detail_url'),
    path('tag/<str:slug>/update/' , TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<str:slug>/delete/', TagDelete.as_view() , name='tag_delete_url'),




]