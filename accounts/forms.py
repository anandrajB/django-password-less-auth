from django import forms
from django.contrib.auth.models import User
from django.http.request import validate_host


class MyCustomuserForm(forms.Form):
    username = forms.CharField(max_length=55,label="enter a username",min_length=3)


    def clean_username(self):
        username = self.cleaned_data["username"].lower()
        r = User.objects.filter(username = username)
        if r.count():
            raise ValueError("username already exists")
        return username

    
    def save(self,commit = True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
        )
        return user
