from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'age', 'email', 'avatar']
