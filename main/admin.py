from django.contrib import admin

from .models import Transaction


class TransactionManager(admin.ModelAdmin):
    list_display = ('id', 'date', 'name', 'amount',
                    'payment_type', 'account', 'status',
                    'starting_amount', 'ending_amount',)
    list_filter = ('date', 'account', 'status', )
    search_fields = ('name', 'date',)


admin.site.register(Transaction, TransactionManager)
