from django import forms

class ThingForm(forms.Form):
    name = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea)
    quantity = forms.IntegerField(widget=forms.NumberInput)
