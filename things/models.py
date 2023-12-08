from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class ThingForm(forms.Form):
    name = forms.CharField(max_length=35)
    description = forms.CharField(widget=forms.Textarea)
    quantity = forms.IntegerField(
        widget=forms.NumberInput,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(50)
        ]
    )
