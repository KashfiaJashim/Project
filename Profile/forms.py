from django import forms
from .models import Profile
from django.forms import ModelForm


class ProfileForm(ModelForm):
    class Meta:
        model = Profile

        fields = ('Full_name', 'email', 'contact_no', 'Profile_pic')
