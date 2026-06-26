from django import forms
from .models import Category, Product


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=255, label='Category name',
                           widget=forms.TextInput(attrs={
                               'class':"input",
                               'placeholder':'Enter category name'
                           }))
    description = forms.CharField(label='Category description',
                                  widget=forms.Textarea(attrs={'placeholder':'Enter category description'}))


    

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    