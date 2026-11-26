from django import forms
from .models import Draft

class DraftForm(forms.ModelForm):
    class Meta:
        model = Draft
        exclude = ()