from django import forms
from .models import SubmitCompetition


class SubmitCompetitionForm(forms.ModelForm):
    class Meta:
        model = SubmitCompetition
        fields = ('competition','title','medium','category','image')