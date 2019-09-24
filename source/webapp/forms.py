from django import forms
from .models import Product


class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, label='Search')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category', 'balance']
