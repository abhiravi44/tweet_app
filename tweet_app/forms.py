from django import forms
from django.contrib.auth import authenticate
from .models import *

from crispy_forms.helper import FormHelper

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    username = forms.CharField(max_length=255, required=True,widget=forms.TextInput(attrs={'placeholder': 'Username','class':'form-control form-control-lg'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Password','class':'form-control form-control-lg'}))

    def clean(self):
        cleaned_data = super().clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user



class PostForm(forms.ModelForm):
    class Meta():
        model=Post
        fields = '__all__'
