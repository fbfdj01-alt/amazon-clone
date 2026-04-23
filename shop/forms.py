from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'image_url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم المنتج'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'وصف المنتج'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'السعر'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'رابط الصورة'}),
        }
