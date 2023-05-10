from django.shortcuts import render
from booksapp.models import Book
from blog.models import Tag
# Create your views here.


def index(request):
    ordering = ['-id']
    books = Book.objects.all()
    tags_1 = Tag.objects.filter(id=2)
    tags_2 = Tag.objects.filter(id=14)
    tags_3 = Tag.objects.filter(id=22)
    tags_4 = Tag.objects.filter(id=23)

    
    context = {
        'books':books,
        'tags_1':tags_1,
        'tags_2':tags_2,
        'tags_3':tags_3,
        'tags_4':tags_4, 
    }
    return render(request , 'pages/index.html', context)

def about(request):
    context = {

    }
    return render(request , 'pages/about.html' , context)

def serch(request):
    context= {

    }
    return render(request , 'pages/serch.html' , context)
