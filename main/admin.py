from django.contrib import admin

from .models import Transaction


class TransactionManager(admin.ModelAdmin):
    list_display = ('id', 'date', 'name', 'amount',
                    'payment_type', 'account', 'status',)
    list_filter = ('date', 'account', 'status', )


admin.site.register(Transaction, TransactionManager)
