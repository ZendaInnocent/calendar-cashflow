from django.utils import timezone

from django.db import models

from accounts.models import User


class Account(models.Model):
    name = models.CharField('Account Name', max_length=50)
    account_type = models.CharField('Account Type', max_length=50)


class Transaction(models.Model):
    STATUS_CHOICES = (
        ('D', 'Deposit'),
        ('W', 'Withdrawal'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Name of the Transaction', max_length=255)
    amount = models.FloatField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    date = models.DateField(default=timezone.now)
    starting_amount = models.FloatField(default=0)
    ending_amount = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
