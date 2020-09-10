from django.contrib import admin

from .models import Transaction


class TransactionManager(admin.ModelAdmin):
    # list_display = ('id', 'user', 'date', 'name', 'amount',
    #                 'payment_type', 'account', 'status',
    #                 'starting_amount', 'ending_amount', )
    list_filter = ('date', 'account', 'status', )
    search_fields = ('name', 'date', )
    readonly_fields = ('starting_amount', 'ending_amount', )


admin.site.register(Transaction, TransactionManager)
