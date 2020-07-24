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
    date = models.DateField(auto_now_add=True)
    starting_amount = models.FloatField(default=0)
    ending_amount = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def get_ending_amount(self):
        ending_amount = self.starting_amount

        if self.status == 'W':
            ending_amount -= self.amount
        elif self.status == 'D':
            ending_amount += self.amount

        return ending_amount

    def save(self, *args, **kwargs):
        self.ending_amount = self.get_ending_amount()
        return super().save(*args, **kwargs)
