from django import forms
from score.models import Score


class ScoreForm(forms.ModelForm):
    class Meta: # class within a class
        model = Score
        fields = ['name', 'value']

