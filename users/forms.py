from django import forms
from django.contrib.auth.models import User

class UserForm(forms.Form):
    username = forms.CharField(min_length=4)
    password = forms.CharField(max_length=100, min_length=8)
    password_confirmation = forms.CharField(max_length=100, min_length=8)

    def clean_username(self):
        data = self.cleaned_data['username']
        if len(User.objects.filter(username = data)) != 0:
            raise forms.ValidationError("username already exists")
        return data

    def clean_password(self):
        data = self.cleaned_data['password']
        if '.' not in data or '_' not in data:
            raise forms.ValidationError('password must contain at least one . and one _')
        return data

    def clean_password_confirmation(self):
        pass2 = self.cleaned_data['password_confirmation']
        if 'password' in self.cleaned_data:
            pass1 = self.cleaned_data['password']

            if pass1 != pass2:
                raise forms.ValidationError("password confirmation does not match")
        return pass2

class LoginForm(forms.Form):
    username = forms.CharField(min_length=4)
    password = forms.CharField(min_length=8,max_length=100)