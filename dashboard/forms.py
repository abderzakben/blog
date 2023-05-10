from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.fields import DateField 
from . models import Homehowork, Notes, Todo ,User
from django.contrib.auth.forms import UserCreationForm
from . models import User



class  NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']

class  DateInput(forms.DateInput):
    input_type = 'date'
    
class HomeworkFrom(forms.ModelForm):
    class Meta:
        model = Homehowork
        widgets = {'due': DateInput()}
        fields = ['subject' , 'title' ,'description','due','is_finished']
class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100 , label="Enter Your Seach : ")

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo 
        fields = ['title', 'is_finished']    




class ConversionForm(forms.Form):
    CHOICES = [

        ('length','Length'),
        ('mass' ,'Mass'),
        
    ]
    maesurement = forms.ChoiceField(choices = CHOICES , widget=forms.RadioSelect)


class ConversionLengthForm(forms.Form):
    CHOICES = [
        ('yard' , 'Yard'),
        ('foot', 'Foot'),
        ] 
    input = forms.CharField(required=False , label=False , widget=forms.TextInput(
        attrs = {'type':'number','placeholder':'Enter the Number'}
    ))  
    measure1 = forms.CharField(
        label = '', widget = forms.Select( choices=CHOICES )
    ) 



class ConversionMassForm(forms.Form):
    CHOICES = [
        ('pound' , 'Pound'),
        ('kilogram', 'Kilogram'),
        ] 
    input = forms.CharField(required=False , label=False , widget=forms.TextInput(
        attrs = {'type':'number','placeholder':'Enter the Number'}
    ))  
    measure2 = forms.CharField(
        label = '', widget = forms.Select( choices=CHOICES )
    ) 
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length = 100, widget = forms.TextInput(attrs={
        'class' : 'form-control', 'placeholder': 'Enter Username'
    }))
    email = forms.CharField(max_length = 100, widget = forms.EmailInput(attrs={
        'class' : 'form-control', 'placeholder': 'Enter Email Address'
    }))
    password1 = forms.CharField(max_length = 100, widget = forms.PasswordInput(attrs={
        'class' : 'form-control', 'placeholder': 'At least eight characters'
    }))
    password2 = forms.CharField(max_length = 100, widget = forms.PasswordInput(attrs={
        'class' : 'form-control', 'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = User
        fields = ['username','email' ,'password1', 'password2']
