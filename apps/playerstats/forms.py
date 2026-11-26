from django import forms
from .models import PlayerGameStat

class PlayerGameStatForm(forms.ModelForm):
    class Meta:
        model = PlayerGameStat
        exclude = ()