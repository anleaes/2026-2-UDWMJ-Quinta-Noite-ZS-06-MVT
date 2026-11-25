from django import forms
from .models

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        exclude = ()