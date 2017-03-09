# -*- encoding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from .models import ProjectBaseInfo, ProjectItemValues 

class SetDataForm(forms.Form):
    key = forms.CharField()
    values = forms.CharField()

class ProjectBaseInfoForm(ModelForm):
    class Meta:
        model = ProjectBaseInfo
        fields = ['pro_name', 'description', 'item_name']

class ProjectItemValuesForm(ModelForm):
    class Meta:
        model = ProjectItemValues
        fields = ['pro_name', 'item_key', 'values']

