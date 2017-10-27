from django import forms
from .models import CityDetails


class CityForm(forms.ModelForm):
    class Meta:
        model = CityDetails
        fields = ('fromcity', 'to', 'date_of_journey', 'return_journey')
