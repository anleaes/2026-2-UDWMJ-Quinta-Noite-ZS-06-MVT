from django import forms
from .models import PlayerGameStats

class PlayerGameStatsForm(forms.ModelForm):
    class Meta:
        model = PlayerGameStats
        exclude = ()