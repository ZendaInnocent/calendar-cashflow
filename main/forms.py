from django import forms

from .models import Transaction


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        exclude = ('user', 'starting_amount', 'ending_amount', )
