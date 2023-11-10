from django import forms
from django.forms import fields
from .models import Comment


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        "name":"message",
        "rows":"3",
        "placeholder":"Join the discussion and leave a comment!"
    }))


    class Meta:
        model = Comment
        fields = ['comment',]
        
        

        