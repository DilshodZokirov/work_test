from django import forms

from core.models import Category


class CategoryForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Title'}))
    description = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Description'}))


class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            "description": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }
