from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class  Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = ("notes")
        verbose_name_plural = ("notes")
    def __str__(self):
        return self.title


 

class Homehowork(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    class  Meta:
        verbose_name = ("homework")
        verbose_name_plural = ("homework")
      

class  Todo(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_finished = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    class  Meta:
        verbose_name = ("Todes")
        verbose_name_plural = ("todo")        

