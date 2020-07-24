import datetime

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models import Sum

from .models import Transaction


@receiver(pre_save, sender=Transaction)
def set_starting_and_ending_amount(sender, instance, **kwargs):
    prev_day_q = Transaction.objects.filter(
        date=instance.date - datetime.timedelta(days=1))

    if prev_day_q:
        starting_amount = prev_day_q.aggregate(
            ending_amount=Sum('ending_amount'))

        instance.starting_amount = starting_amount['ending_amount']

    else:
        instance.starting_amount = 0

    amount = instance.starting_amount

    if instance.status == 'D':
        amount += instance.amount
    elif instance.status == 'W':
        amount -= instance.amount

    instance.ending_amount = amount
