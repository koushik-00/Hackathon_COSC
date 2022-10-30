from django import forms

from loginapp.models import login 
class loForm(forms.ModelForm):
    class Meta: 
        model=login
        fields= '__all__'

