from django import forms
from .models import Bookmark

class BlogUpdate(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ['title','url']