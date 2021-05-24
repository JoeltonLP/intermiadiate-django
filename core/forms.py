from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='name')
    email = forms.EmailField(label='email')
    subject = forms.CharField(label='subject')
    message = forms.CharField(label='name')

