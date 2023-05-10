from django.db import models
from django.contrib.auth.models import User
from datetime import datetime , date
from django.shortcuts import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField  
from time import time
from datetime import datetime




def gen_slug(s):
    slug = slugify(s , allow_unicode=True)
    return slug + f'-{int(time())}'

   

class Post(models.Model):
    title = models.CharField(max_length=150 , db_index=True )
    slug = models.SlugField(max_length = 150 , unique=True , blank=True)
    body = RichTextField(blank=True , null=True ) 
    post_date = models.DateField(auto_now_add = True)
    tags = models.ManyToManyField('Tag' , blank=True , related_name='posts')
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail_url' , kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse( 'post_delete_url' , kwargs={'slug':self.slug})    


    def save(self , *args , **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title) 
        super().save(*args , **kwargs)
               
    class Meta:
        ordering = ['-id']

class Tag(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150 , unique=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('tag_detail_url' , kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('tag_update_url' , kwargs={'slug':self.slug})
        
    def get_delete_url(self):
        return reverse('tag_delete_url' , kwargs={'slug':self.slug})            

    
class Comment(models.Model):
    post = models.ForeignKey(Post , related_name="comment" ,  on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return '%s - %s' % (self.post.title , self.name  )

