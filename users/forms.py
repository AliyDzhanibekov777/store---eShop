from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2',
        'placeholder': "Введите имя пользователя",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-2',
        'placeholder': "Введите пароль",
    }))
    
    
    class Meta:
        model = User
        fields = ('username', 'password')
        
        
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2',
        'placeholder': "Введите имя",
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2',
        'placeholder': "Введите фамилию",
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2',
        'placeholder': "Введите имя пользователя",
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-2',
        'placeholder': "Введите адрес эл. почты",
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-2',
        'placeholder': "Введите пароль",
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-2',
        'placeholder': "Введите пароль повторно",
    }))
    
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        
        
class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2',
        'readonly': True,
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-2',
    }))
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')