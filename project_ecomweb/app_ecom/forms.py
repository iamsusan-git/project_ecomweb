from django import forms
from .models import Product, Category

class ProductAddForm(forms.ModelForm):
    class Meta:
        #fields = '__all__' #for all field
        fields = ("title", "desc","price","category","quantity","discount","cod") #for selective field
        model = Product

class CategoryAddForm(forms.ModelForm):
    class Meta:
        fields = ("category_name",)
        model = Category
        