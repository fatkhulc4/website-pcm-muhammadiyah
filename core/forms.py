from django import forms

from .models import IncomingMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = IncomingMessage
        fields = ["name", "email", "subject", "message"]
        labels = {
            "name": "Nama",
            "email": "Email",
            "subject": "Subjek",
            "message": "Pesan",
        }
        widgets = {"message": forms.Textarea(attrs={"rows": 5})}

    def clean_message(self):
        message = self.cleaned_data["message"].strip()
        if len(message) < 10:
            raise forms.ValidationError("Pesan minimal 10 karakter.")
        return message
