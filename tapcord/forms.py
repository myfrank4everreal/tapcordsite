from django.forms import ModelForm
from django import forms
from .models import NewsLetterMember




class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'text-field form-control validate-field required', 'placeholder':'Full Name', "name":"name", "id":"form-name", "data-validation-type":"string", 'type':"text"}
            )
        )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'class':'text-field form-control validate-field required', 'placeholder':'Email Address', "name":"email", "id":"form-email", "data-validation-type":"email", "type":"email"}
            )
        )
    contact_number = forms.CharField(
        widget=forms.NumberInput(
            attrs={'class':'text-field form-control validate-field phone', 'placeholder':'Contact number', "name":"contact_number", "id":"form-contact-number", "data-validation-type":"phone", "type":"tel"}
            )
        )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'class':'text-field form-control validate-field required', 'placeholder':'Messsage', "name":"message", "type":"textarea"}
            )
        )

# class ContactForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
#     sender = forms.EmailField()
#     cc_myself = forms.BooleanField(required=False)

class NewsLetterMemberForm(ModelForm):
    email = forms.CharField(widget=forms.Textarea(attrs={
            'class':'form-control',
            "name":"message",
            "rows":"3",
            "placeholder":"Join the discussion and leave a comment!"
        }))

    class Meta:
        model = NewsLetterMember
        fields = ['email',]



