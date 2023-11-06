from django import forms




class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    contact_number = forms.CharField(widget=forms.NumberInput)
    message = forms.CharField(widget=forms.Textarea)

# class ContactForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
#     sender = forms.EmailField()
#     cc_myself = forms.BooleanField(required=False)
