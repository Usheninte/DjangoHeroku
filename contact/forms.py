from django import forms

from .models import ContactInfo


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['email', 'full_name', 'subject', 'message']
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email address',
                }
            ),
            'full_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Full name',
                }
            ),
            'subject': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Subject',
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Hello, could I get more information on ...',
                    'rows': '5',
                }
            ),
        }
