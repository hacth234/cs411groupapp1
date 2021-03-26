from django import forms
from .models import *

# class IngredientForm(forms.ModelForm):
#     """ A form to search a recipe"""
#     ingredient = forms.CharField(label="Enter Ingredient You Want to make a dish with", required=True)
#     class Meta:
#         model = RecipeIngredients
#         fields = ['ingredient']
        
# class DishForm(forms.ModelForm):
#     """ A form to search a dish"""
#     dish = forms.CharField(label="Enter Ingredient You Want to make a dish with", required=True)
#     class Meta:
#         model = RecipeDish
#         fields = ['dish']

class CreateSearchRecipeForm(forms.ModelForm):
    dish = forms.CharField(label="Enter the Dish", required=True)
    ingredient = forms.CharField(label="Enter Ingredient You Want to make a dish with", required=True)
    class Meta:
        model = Recipe
        fields = ['dish', 'ingredient']

class CreateSearchSymptomForm(forms.ModelForm):
    symptom = forms.CharField(label="Enter the symptom you want to avoid", required=True)
    class Meta:
        model = Symptom
        fields = ['symptom']