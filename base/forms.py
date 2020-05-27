from django import forms

from .models import Dict

class GetDict(forms.ModelForm):
    class Meta:
        model = Dict
        fields = ("englishWord","rush")

class SendDict(forms.ModelForm):
    file = forms.FileField()
    class Meta:
        model = Dict
        fields = ("file",)