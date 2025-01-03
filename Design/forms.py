from django import forms
from .models import Language,UserMst

class languageform(forms.ModelForm):
    class Meta:
        model=Language
        fields='__all__'

class userform(forms.ModelForm):
    class Meta:
        model=UserMst
        fields='__all__'