# -*- encoding: utf-8 -*-

from django import forms 

class SetDataForm(forms.Form):
    key = forms.CharField()
    values = forms.CharField()



