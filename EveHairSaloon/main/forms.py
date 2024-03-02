from .models import Customer, Product, Order, OrderDetail, Payment, Review, Cart
from django.forms import ModelForm
from django import forms


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'quantity_available', 'images')
        label = {'name': 'Product Name', 'description': 'Product Description', 'price':'Product Price', 'quantity_available':'Quantity','images':'Product Image'}
        widgets ={ 

            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Product Name'}),
            'description' : forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Product Description','rows':'2'}),
            'price' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'R99,10'}),
            'quantity_available' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'197'}),
            'images': forms.FileInput(attrs={'class': 'form-control'}),
            
        }



