from django import forms

from .models import ContactInfo


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['email', 'full_name', 'subject', 'message']
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'full_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'subject': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
