from django import forms
from accountant.models import Applications


class ApplicationsForm(forms.ModelForm):
    class Meta:
        model = Applications
        fields = ['name', 'phone', 'email', 'activity', 'organizational_form', 'tax_system']
