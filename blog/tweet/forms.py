from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tweet
from django.contrib.auth.forms import AuthenticationForm

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

class CustomLoginForm(AuthenticationForm):
     def __init__(self, request = ..., *args, **kwargs):
         super().__init__(request, *args, **kwargs)
         for field in self.fields:
             self.fields[field].widget.attrs.update({'class':'form-control', 'placeholder':f'Enter your {field}'})
