from django import forms
from django.core.exceptions import ValidationError
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','slug','body','image','price']

        widgets = {
        'title':forms.TextInput(attrs={'class':'form-control'}),
        'slug':forms.TextInput(attrs={'class':'form-control'}),
        'body':forms.Textarea(attrs={'class':'form-control'}),
        'image':forms.FileInput(attrs={'class':'form-control'}),
        'price':forms.NumberInput(attrs={'class':'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug =='create':
            raise ValidationError('Slug may not be "create"')
        return new_slug
