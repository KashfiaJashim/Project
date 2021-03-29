from django import forms
from .models import SubmitCompetition, Review


class SubmitCompetitionForm(forms.ModelForm):
    class Meta:
        model = SubmitCompetition
        fields = ('competition', 'title', 'medium', 'category', 'image')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'comment')
