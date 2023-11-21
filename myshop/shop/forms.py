from django import forms
from .models import Product, ProductCategory, Provider, Review


class ProductForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=ProductCategory.objects.all())
    class Meta:
        model = Product
        fields = ['name', 'price', 'vendor_code', 'categories']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'rate_field']

# class ProviderForm(forms.Form):
#     provider = forms.ChoiceField()
#     def __init__(self, *args, **kwargs):
#         choices = kwargs.pop('choices', [])
#         super(ProviderForm, self).__init__(*args, **kwargs)
#         self.fields['provider'].choices = choices
