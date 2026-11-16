from django import forms

from .models import IncomingMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = IncomingMessage
        fields = ["name", "email", "subject", "message"]
        labels = {
            "name": "Nama lengkap",
            "email": "Alamat email",
            "subject": "Subjek",
            "message": "Pesan",
        }
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Nama Anda"}),
            "email": forms.EmailInput(attrs={"placeholder": "nama@email.com"}),
            "subject": forms.TextInput(attrs={"placeholder": "Tujuan pesan Anda"}),
            "message": forms.Textarea(
                attrs={"rows": 6, "placeholder": "Tulis pesan Anda (minimal 10 karakter)"}
            ),
        }

    def clean_message(self):
        message = self.cleaned_data["message"].strip()
        if len(message) < 10:
            raise forms.ValidationError("Pesan minimal 10 karakter.")
        return message
