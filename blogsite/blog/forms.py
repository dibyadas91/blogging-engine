from django import forms
from django.forms.widgets import Textarea


class Contact(forms.Form):

    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=Textarea())