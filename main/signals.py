import datetime

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models import Sum

from .models import Transaction


@receiver(pre_save, sender=Transaction)
def set_starting_and_ending_amount(sender, instance, **kwargs):
    prev_transaction = Transaction.objects.last()

    if prev_transaction:
        instance.starting_amount = prev_transaction.ending_amount
    else:
        instance.starting_amount = 0

    amount = instance.starting_amount

    if instance.status == 'D':
        amount += instance.amount
    elif instance.status == 'W':
        amount -= instance.amount

    instance.ending_amount = amount
