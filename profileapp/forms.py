from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# from .models import Profile
from django.forms.models import ModelForm

from django.forms.widgets import FileInput
from numpy import char

class CreateUserForm(UserCreationForm):
    address = forms.CharField( max_length=250, required=False)
    phone = forms.IntegerField(required=False)
    first_name = forms.CharField( max_length=100, required=False)
    last_name = forms.CharField( max_length=100, required=False)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'address', 'phone','password1', 'password2', 'first_name', 'last_name')


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
