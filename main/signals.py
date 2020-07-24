import datetime

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models import Sum

from .models import Transaction


@receiver(pre_save, sender=Transaction)
def set_starting_amount(sender, instance, **kwargs):
    past_date = instance.date - datetime.timedelta(days=1)
    if Transaction.objects.filter(date=past_date):
        starting_amount = Transaction.objects.filter(past_date).aggregate(
            ending_amount=Sum('ending_amount'))

        instance.starting_amount = starting_amount['ending_amount']

    else:
        instance.starting_amount = 0
