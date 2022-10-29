from django import forms
from ecapp.models import course

class ceform(forms.ModelForm):
    class Meta:
        model=course
        fields='__all__'