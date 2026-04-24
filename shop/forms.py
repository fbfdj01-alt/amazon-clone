from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'image']
        labels = {
            'title': 'اسم المنتج',
            'description': 'الوصف',
            'price': 'السعر',
            'image': 'صورة المنتج',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل اسم المنتج'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'اكتب وصفاً قصيراً'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
