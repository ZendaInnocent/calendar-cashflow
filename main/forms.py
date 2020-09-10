from django import forms
from django.core.mail import send_mail

from .models import Transaction, Account


class DateInput(forms.DateInput):
    input_type = 'date'


class TransactionForm(forms.ModelForm):
    # todo: return only accounts created by the user
    account = forms.ModelChoiceField(Account.objects.all(),
                                     empty_label='Choose Account')

    class Meta:
        model = Transaction
        exclude = ('user', 'starting_amount', 'ending_amount', )
        widgets = {
            'date': DateInput(),
        }


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your Name',
        })
    )
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            'placeholder': "Your Message (Not less than 4 words)",
            'rows': '4',
        }
    ))

    def clean_message(self):
        message = self.cleaned_data.get('message', '')
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message

    def send_mail(self):
        message = (f"From: {self.cleaned_data['name']}\n\n"
                   f"Message:\n{self.cleaned_data['message']}")

        send_mail(
            'Mail from the site',
            message,
            'contact@domain.com',
            ['zendainnocent@protonmail.com'],
            fail_silently=False,
        )
