from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display  = ['name', 'type', 'category', 'status', 'amount', 'date']
    list_filter   = ['type', 'category', 'status']
    search_fields = ['name', 'description']
    list_editable = ['status']