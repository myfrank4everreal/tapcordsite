from django import forms
from django.forms import fields 
from .models import Comment, BlogPost 
from ckeditor.widgets import CKEditorWidget





class BlogPostForm(forms.ModelForm):

    description= forms.CharField(widget=CKEditorWidget())

    class meta:
        model = BlogPost

        fields = ['title', 'image', 'description',]


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
        
        

        