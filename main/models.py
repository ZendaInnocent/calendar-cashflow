import datetime

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
    name = models.CharField(max_length=255, help_text="Name of the Transaction")
    amount = models.PositiveIntegerField()
    payment_type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    account = models.CharField(max_length=3, choices=ACCOUNT_CHOICES)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    # TO-DO
    # date should be added automatically when item created
    # date = models.DateField(auto_now_add=True)
    # Now is for testing purpose only
    date = models.DateField(default=datetime.date.today())
    starting_amount = models.FloatField(default=0)
    ending_amount = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
