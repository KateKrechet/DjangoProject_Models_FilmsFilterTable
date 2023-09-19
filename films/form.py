from django import forms
from .models import *


class FilterCountry(forms.Form):
    country = forms.CharField(label="Фильтр по стране")


class FilterYear(forms.Form):
    year = forms.IntegerField(label='Фильтр по году', min_value=1, max_value=2023)


class DoubleFilter(forms.Form):
    country = forms.CharField(label="Фильтр по стране")
    year = forms.IntegerField(label='Фильтр по году', min_value=1, max_value=2023)
