from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

        widgets={
            'name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter your name'
            }),
            'email': forms.EmailInput(attrs={
                'class':'form-control'
            }),
            'body': forms.Textarea(attrs={
                'class':'form-control'
            })
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']