from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'phone', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ad Soyad'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon Numaranız'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-posta (isteğe bağlı)'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mesajınız', 'rows': 4}),
        }