from django.shortcuts import render
from .forms import ThingForm

from django import forms  # 添加这一行以正确导入 forms 模块



def home(request):
    form = ThingForm()
    return render(request, 'home.html', {'form': form})




class ThingForm(forms.Form):
    name = forms.CharField(max_length=35)
    description = forms.CharField(widget=forms.Textarea(attrs={'maxlength': '120'}))  # 设置 description 字段的最大长度为 120，同时使用 Textarea 将其渲染成多行文本框
    quantity = forms.IntegerField(widget=forms.NumberInput)

