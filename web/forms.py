from django import forms
from django.forms.widgets import EmailInput
from django.forms.widgets import Textarea
from django.forms.widgets import TextInput

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ()
        widgets = {
            "name": TextInput(
                attrs={
                    "type": "text",
                    "name": "name",
                    "class": "form-control",
                    "id": "contactFormFullName",
                    "placeholder": "Enter your full name",
                }
            ),
            "email": EmailInput(
                attrs={
                    "type": "email",
                    "class": "form-control",
                    "id": "contactFormEmail",
                    "placeholder": "Your Email*",
                    "name": "Enter your email address",
                }
            ),
            "message": Textarea(
                attrs={
                    "name": "message",
                    "class": "form-control",
                    "id": "exampleInputMessage1",
                    "placeholder": "Enter your message...",
                }
            ),
        }
