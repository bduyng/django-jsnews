from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms


# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        max_length=254,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'username',
            'placeholder': 'Username',
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
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'] = forms.CharField(
            label='Username',
            max_length=254,
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'username',
                'placeholder': 'Username',
                'type': 'text'
            })
        )
        self.fields['password1'] = forms.CharField(
            label='Password',
            max_length=254,
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'password',
                'placeholder': 'Password',
                'type': 'password'
            })
        )
        self.fields['password2'] = forms.CharField(
            label='Password Confirmation',
            max_length=254,
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'password',
                'placeholder': 'Password Confirmation',
                'type': 'password'
            })
        )
