from django.shortcuts import render
from .forms import ThingForm

from django import forms  # 添加这一行以正确导入 forms 模块



def home(request):
    form = ThingForm()
    return render(request, 'home.html', {'form': form})




class ThingForm(forms.Form):
    name = forms.CharField(max_length=35)
    description = forms.CharField(widget=forms.Textarea(attrs={'maxlength': '120'}))
    quantity = forms.IntegerField(widget=forms.NumberInput)

