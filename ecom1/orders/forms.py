from django import forms
from .models import Location,staff_contractor_company,assset_tracker_activity
from django.forms import ModelForm


    
class staff_contractor_companyForm(forms.ModelForm):
    class Meta:
        model=staff_contractor_company
        exclude = ['user']

class assset_tracker_activityForm(forms.ModelForm):
    class Meta:
        model=assset_tracker_activity
        exclude=['returned','asset_tracking_id','user']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['location']