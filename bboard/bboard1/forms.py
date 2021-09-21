from django import forms
from django.contrib.auth.views import LoginView, LogoutView
from .models import Bb
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BbForm(forms.ModelForm):
    class Meta:
        model=Bb
        fields=('title', 'content', 'price', 'rubric')

class RegistForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='This field is required')
    class Meta:
        # Свойство модели User
        model = User
        # Свойство назначения полей
        fields = ('username', 'email', 'password1', 'password2',)
