from django import forms
from .models import Play


class PlayForm(forms.ModelForm):
    class Meta:
        model = Play
        fields = ['title', 'type', 'dead_line']