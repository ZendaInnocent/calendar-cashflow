from django.contrib import admin

from .models import Transaction, Account

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'name', 'amount',
                    'account', 'status',
                    'starting_amount', 'ending_amount', )
    list_display_links = ('user', 'date', 'name', )
    list_filter = ('date', 'account', 'status', )
    search_fields = ('name', 'date', )
    readonly_fields = ('starting_amount', 'ending_amount', )


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass
