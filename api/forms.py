from django import forms
from django.forms import TextInput, Textarea, PasswordInput, EmailInput
from .models import Store, User, AdminUser


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('name', 'description', 'image', 'address', 'country', 'latitude', 'longitude', 'categories')
        widgets = {
            'name': TextInput(attrs={'class': 'u-full-width', 'placeholder': 'Store name'}),
            'latitude': TextInput(attrs={'class': 'u-full-width', 'placeholder': 'Latitude'}),
            'longitude': TextInput(attrs={'class': 'u-full-width', 'placeholder': 'Longitude'}),
            'address': Textarea(attrs={'class': 'u-full-width', 'placeholder': 'Address'}),
            'description': Textarea(attrs={'class': 'u-full-width', 'placeholder': 'Description'}),
            'categories': Textarea(attrs={'class': 'u-full-width', 'placeholder': 'Categories comma separated value'})
        }


class LoginForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'autocomplete': 'off',
            'style': 'width:300px;',
            'placeholder': ('xyz@email.com'),
            'required': 'required'
        }),
        error_messages={'invalid': 'Please enter a valid email address'}
    )

    class Meta:
        model = AdminUser
        fields = ('email', 'password')
        widgets = {
            'password': PasswordInput(attrs={'placeholder': 'Password', 'style': 'width:300px;'})
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = AdminUser
        fields = ('name', 'email', 'password')
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Display Name'}),
            'password': PasswordInput(attrs={'placeholder': 'New password'})
        }
