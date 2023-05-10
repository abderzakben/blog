from django.shortcuts import render , redirect
from django.shortcuts import  get_object_or_404 , reverse
from .models import Post , Tag




class DetailObjectMixin:
    model = None
    template = None
    def get(self, request , slug):
        #obj = self.model.Post.objects.get(slug__iexact=slug)
        obj = get_object_or_404(self.model, slug__iexact=slug) 
        context = {
            self.model.__name__.lower():obj,
            'admin_object': obj,
        }
        return render(request, self.template  , context )

class CreateObjectMixin:
    model = None 
    template = None 

    def get(self , request):
        form = self.model
        return render(request , self.template , context={'form' : form})
    def post(self, request):
        bound_form = self.model(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect('home-blog')
        return render(request , self.template , context={'form':bound_form})    

class UpdateObjectMixin:
    model = None
    template = None
    form_class = None
    redirect_url = None 

     
    def get(self, request , slug):
        obj  = get_object_or_404(self.model , slug__iexact=slug)
        bound_form = self.form_class(instance=obj)
        context = {
            'form':bound_form,
            self.model.__name__.lower():obj,

        }
        return render(request, self.template , context )

    def post(self , request , slug):
        obj = get_object_or_404(self.model , slug__iexact=slug)
        bound_form = self.form_class( request.POST , instance=obj)

        if bound_form.is_valid():
            bound_form.save()
            return redirect(reverse(self.redirect_url)) 
        context = {
            'form':bound_form,
            self.model.__name__.lower():obj,

        }    
        return render(request, self.template , context) 


class DeleteObjectMixin:
    model = None
    template = None 
    redirect_url = None 
 
    def get(self , request , slug):
        obj  = get_object_or_404( self.model  , slug__iexact=slug)
        return render(request , self.template , context={self.model.__name__.lower():obj })
    def post(self , request , slug):
        obj = get_object_or_404( self.model , slug__iexact=slug)
        obj.delete() 
        return redirect(reverse(self.redirect_url))               