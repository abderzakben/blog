from django.shortcuts import render , redirect , get_object_or_404
from django.shortcuts import reverse  
from django.http import HttpResponseRedirect
from django.views.generic import  View , CreateView
from django.db.models import Q
from django.contrib.auth.mixins import  LoginRequiredMixin 
from .forms import TagForm , PostForm , CommentForm
from .models import Post , Tag , Comment
from .utils import DetailObjectMixin , CreateObjectMixin  , UpdateObjectMixin , DeleteObjectMixin
from django.urls import reverse_lazy
# Create your views here.



def home(request):
    search_query = request.GET.get('search' , '')
    if  search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()
    context={
        'posts':posts, 
       }
    return render(request, 'blog/home.html', context)






def tags_list(request):
    tags = Tag.objects.all()
    context={
         'tags':tags
         }
    return render(request , 'blog/tags_list.html',context)


class PostDetail(DetailObjectMixin,View):
    model = Post 
    template = 'blog/post_detail.html'
    ordering = ['-id'] 


class TagDetail(DetailObjectMixin,View):
    model = Tag 
    template = 'blog/tag_detail.html'
    ordering = ['-id']


class TagCreate(LoginRequiredMixin , CreateObjectMixin , View):
    model = TagForm
    template = 'blog/tag_create.html'

           

class PostCreate(LoginRequiredMixin , CreateObjectMixin,View):
    model = PostForm
    template = 'blog/post_create.html' 

class TagUpdate(LoginRequiredMixin ,UpdateObjectMixin,View):
    model = Tag 
    template =   'blog/tag_update.html'
    form_class = TagForm 

class PostUpdate(LoginRequiredMixin , UpdateObjectMixin, View):
    model = Post 
    template = 'blog/post_update.html'
    form_class = PostForm 
    redirect_url = 'home-blog'


class TagDelete(LoginRequiredMixin, DeleteObjectMixin,View):
    model = Tag
    template = 'blog/tag_delete.html' 
    redirect_url = 'blog/tags/' 
      
class PostDelete(LoginRequiredMixin,DeleteObjectMixin,View):
    model = Post
    template = 'blog/post_detele.html'
    redirect_url = 'home-blog'

class AddCommentbView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_commenter.html'
    redirect_url = 'post_detail_url'
    #fields = '__all__'

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home-blog')

        







