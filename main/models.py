import datetime

from django.db import models


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

    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    payment_type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    account = models.CharField(max_length=3, choices=ACCOUNT_CHOICES)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    date = models.DateField()
    starting_amount = models.FloatField(default=0)
    ending_amount = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
