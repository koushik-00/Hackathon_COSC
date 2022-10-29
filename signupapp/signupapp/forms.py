from django import forms
from signupapp.models import details

class DetailsForm(forms.ModelForm):
    class Meta:
        model=details
        fields='__all__'
