# from django.contrib.auth.models import User
from .models import CustomUser as User, Contact
from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    
class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ('email', 'full_name', 'subject', 'message', )