from django.shortcuts import render
from django.http import request
from django.shortcuts import render , redirect
from . models import Book ,Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib import  messages 
from django.contrib import  auth

# Create your views here.


def books(request):
    recommended_books =Book.objects.filter(recommended_books = True)
    fiction_books  =Book.objects.filter(fiction_books = True)
    business_books =Book.objects.filter(business_books= True)

    context = {
        'recommended_books':recommended_books,
        'fiction_books':fiction_books,
        'business_books':business_books,
    }
    return render(request , 'booksapp/books.html' , context )


def all_books(request):
    books = Book.objects.all()
    
    context = {
        'books':books,
        
    }
    return render(request , 'booksapp/all_books.html' , context)

def category_detail(request,slug):
    category = Category.objects.get(slug=slug)
    context = {
         'category':category
    }
    return render(request , 'booksapp/genre_detail.html' , context)  

def book_detail(request, slug):
    book = Book.objects.get(slug = slug)
    book_category = book.category.first()
    similar_books = Book.objects.filter(category__name__startswith = book_category)
    context = {
        'book':book,
        'similar_books':similar_books,

    }
    return render(request, 'booksapp/book_detail.html' , context)      
