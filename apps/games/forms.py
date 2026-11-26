from django import forms
from .forms import GameForm

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ()