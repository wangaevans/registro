from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from django.forms import ModelForm


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'avatar', 'bio',]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'text-gray-600'}),
            'first_name': forms.TextInput(attrs={'class': 'text-gray-600'}),
            'last_name': forms.TextInput(attrs={'class': 'text-gray-600'}),
            'email': forms.EmailInput(attrs={'class': 'text-gray-600'}),
            'bio': forms.Textarea(attrs={'class': 'text-gray-600'}),
        }

class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email',
                  'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'rounded'}),
            'email': forms.EmailInput(attrs={'class': 'rounded'}),
        }
