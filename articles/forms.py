from django.contrib.auth.forms import AuthenticationForm
from django import forms


# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Email',
        max_length=254,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'username',
            'placeholder': 'Email',
            'type': 'text'
        })
    )
    password = forms.CharField(
        label='Password',
        max_length=254,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'password',
            'placeholder': 'Password',
            'type': 'password'
        })
    )
