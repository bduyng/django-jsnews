from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
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


class RegisterForm(UserCreationForm):
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
        password1 = forms.CharField(
            label='Password',
            max_length=254,
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'password',
                'placeholder': 'Password',
                'type': 'password'
            })
        )
        password2 = forms.CharField(
            label='Password Confirmation',
            max_length=254,
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'password',
                'placeholder': 'Password Confirmation',
                'type': 'password'
            })
        )
