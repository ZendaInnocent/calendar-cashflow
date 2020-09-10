from django.utils import timezone

from django.db import models

from accounts.models import User


class Transaction(models.Model):
    TYPE_CHOICES = (
        ('CH', 'Check'),
        ('CA', 'Cash'),
        ('PA', 'Payment'),
    )

    ACCOUNT_CHOICES = (
        ('BOZ', 'Bank Of Fredders'),
        ('BI', 'Building & Construction'),
        ('C', 'Cash'),
        ('CA', 'Checking Account'),
        ('EQ', 'Equipments'),
        ('IP', 'Insurance Paid'),
        ('LAM', 'Less Accum. Depreciation'),
        ('PC', 'Petty Cash'),
        ('SU', 'Supplies'),
    )

    STATUS_CHOICES = (
        ('D', 'Deposit'),
        ('W', 'Withdrawal'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Name of the Transaction', max_length=255)
    amount = models.FloatField()
    payment_type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    account = models.CharField(max_length=3, choices=ACCOUNT_CHOICES)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    date = models.DateField(default=timezone.now)
    starting_amount = models.FloatField(default=0)
    ending_amount = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
