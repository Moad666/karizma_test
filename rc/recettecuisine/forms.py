# forms.py
from django import forms
from .models import Recette

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ['title', 'dureePreparation', 'ingredients', 'image_url', 'etapePreparation']
