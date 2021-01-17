from django import forms
from .models import Register

class reg_forms(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['first_name', 'last_name', 'email', 'phone', 'password', 'city', 'state', 'country']