from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import CharField, TextInput, EmailInput, EmailField, PasswordInput

class RegistrationForm(UserCreationForm):
    username = CharField(max_length=30, min_length=3, required=True, widget=TextInput(attrs={'placeholder': 'Username', "class": "form-control"}))
    email = EmailField(required=True, widget=EmailInput(attrs={'placeholder': 'Email', "class": "form-control"}))
    password1 = PasswordInput(attrs={'placeholder': 'Password', "class": "form-control"})
    password2 = PasswordInput(attrs={'placeholder': 'Confirm Password', "class": "form-control"})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = CharField(max_length=30, min_length=3, required=True, widget=TextInput(attrs={'placeholder': 'Username', "class": "form-control"}))
    password = PasswordInput(attrs={'placeholder': 'Password', "class": "form-control"})

    class Meta:
        model = User
        fields = ['username', 'password']