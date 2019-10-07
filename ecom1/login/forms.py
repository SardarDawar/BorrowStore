from django import forms
from .models import staff_contractor

class staff_contractor_form(forms.ModelForm):
    class Meta:
        model = staff_contractor
        exclude = ['staff_contractor_company_id','archive','user']