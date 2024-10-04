from django import forms
from .models import Categoria

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
