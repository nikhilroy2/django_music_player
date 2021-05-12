from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from django.forms import ModelForm
from .models import AlbumMusic
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = {"first_name", "last_name", "username","email","password1","password2"}
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class AlbumMusicForm(forms.ModelForm):
    upload_thumbnail = forms.ImageField(required=False)
    class Meta:
        model = AlbumMusic
        fields = "__all__"