from django import forms
from .models import Cargo,Area,Empleado
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields='__all__'

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model= User
        fields = ["username", "groups", "password1", "password2"]
        
class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()