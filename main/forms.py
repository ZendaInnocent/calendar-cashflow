from django import forms

from .models import Transaction


class TransactionForm(forms.ModelForm):
    date = forms.CharField(widget=forms.DateInput)

    class Meta:
        model = Transaction
        exclude = ('starting_amount', 'ending_amount', )
