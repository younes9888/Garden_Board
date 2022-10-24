from dataclasses import field
from msilib.schema import Class
from sqlite3 import Row
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    content=forms.CharField(widget=forms.Textarea(attrs={'rows':4} ))
    
    class Meta:
        model=Comment
        fields=('content',)
