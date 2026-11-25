from django import forms
from .models import Champion

class ChampionForm(forms.ModelForm):
    class Meta:
        model = Champion
        exclude = ()