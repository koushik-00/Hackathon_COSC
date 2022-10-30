from django import forms
from signupapp.models import details,login

class loForm(forms.ModelForm):
    class Meta: 
        model=login
        fields= '__all__'


class DetailsForm(forms.ModelForm):
    class Meta:
        model=details
        fields='__all__'

        def clean(self):
            cleaned_data = super().clean()
            p1=self.cleaned_data['Password']
            p2=self.cleaned_data['ConfirmPassword']
            if p1!=p2:
                raise forms.ValidationError('Password does not match')
