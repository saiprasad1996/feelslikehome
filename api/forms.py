from django import forms
from django.forms import TextInput, Textarea
from .models import Store


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('name', 'description', 'image', 'address', 'country', 'latitude', 'longitude','categories')
        widgets = {
            'name': TextInput(attrs={'class': 'u-full-width', 'placeholder': 'Store name'}),
            'latitude': TextInput(attrs={'class': 'u-full-width', 'placeholder': 'Latitude'}),
            'longitude': TextInput(attrs={'class': 'u-full-width', 'placeholder': 'Longitude'}),
            'address': Textarea(attrs={'class': 'u-full-width', 'placeholder': 'Address'}),
            'description': Textarea(attrs={'class': 'u-full-width', 'placeholder': 'Description'}),
            'categories': Textarea(attrs={'class':'u-full-width','placeholder':'Categories comma separated value','disabled':'true'})
        }
