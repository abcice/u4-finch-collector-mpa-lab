from django import forms
from .models import EscapeAttempt

class EscapeAttemptForm(forms.ModelForm):
    class Meta:
        model = EscapeAttempt
        fields = ['date', 'method', 'success']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%dT%H:%M'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
            'method': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. tunnel, fake mustache, bribe the farmer',
                    'class': 'method-input'
                }
            ),
            'success': forms.CheckboxInput(
                attrs={
                    'title': "Did our feathered Houdini actually make it?"
                }
            )
        }
        labels = {
            'date': "Date & Time of the Daring Escape",
            'method': "Escape Method (a.k.a. terrible plan)",
            'success': "Did They Make It? (Spoiler: probably not)"
        
        }