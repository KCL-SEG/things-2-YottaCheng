from django.shortcuts import render

from django import forms  # 添加这一行以正确导入 forms 模块



def home(request):
    form = ThingForm()
    return render(request, 'home.html', {'form': form})




class ThingForm(forms.Form):
    name = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea)
    quantity = forms.IntegerField(widget=forms.NumberInput)
