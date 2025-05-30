from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'message': 'Your Message',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')

    # Normalize to lowercase
        email = email.lower()

    # 1. Check email domain
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Email must end with '@gmail.com'.")

    # 2. Check if already submitted
        if Inquiry.objects.filter(email=email).exists():
            raise forms.ValidationError("This email has already submitted a message.")

        return email