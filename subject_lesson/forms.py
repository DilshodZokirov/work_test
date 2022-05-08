from django import forms
from .models import SubjectLesson


class SubjectLessonForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Title'}))
    description = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Description'}))
    video = forms.FileField(widget=forms.FileInput(
        attrs={'class': "form-control", 'name': 'lesson video'}
    ))


class SubjectLessonUpdateForm(forms.ModelForm):
    class Meta:
        model = SubjectLesson
        fields = ['title', 'description', 'video']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            "description": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            "video": forms.FileInput(attrs={'class': 'form-control', 'name': 'lesson video'}),
        }
