from django import forms

from loginapp.models import login 
class stForm(forms.ModelForm):
    class Meta: 
        model=login
        fields= '__all__'

