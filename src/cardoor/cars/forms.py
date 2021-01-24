from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:

        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2')

        widgets = {
            'username': forms.fields.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.fields.TextInput(attrs={'placeholder': 'Email'}),
            'first_name': forms.fields.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.fields.TextInput(attrs={'placeholder': 'Last Name'}),
        }
