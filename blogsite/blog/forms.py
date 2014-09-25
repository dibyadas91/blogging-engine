from django import forms
from django.forms.widgets import Textarea


class ContactForm(forms.Form):

    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(widget=Textarea())
    email = forms.EmailField()
