from django import forms
from .models import Comment,Comment_garden,Comment_garden_tips

class CommentForm(forms.ModelForm):
    content=forms.CharField(widget=forms.Textarea(attrs=
    {'class':'md-textarea form-control', 'placeholder':'comment here..', 'rows':4} ))

    class Meta:
        model=Comment
        fields=('content',)

class CommentForm_garden(forms.ModelForm):
    content=forms.CharField(widget=forms.Textarea(attrs=
    {'class':'md-textarea form-control', 'placeholder':'comment here..', 'rows':4} ))

    class Meta:
        model=Comment_garden
        fields=('content',)

class CommentForm_garden_tips(forms.ModelForm):
    content=forms.CharField(widget=forms.Textarea(attrs=
    {'class':'md-textarea form-control', 'placeholder':'comment here..', 'rows':4} ))

    class Meta:
        model=Comment_garden_tips
        fields=('content',)
