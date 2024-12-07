from django.contrib import admin
from .models import Expenditure, ExpenseType

@admin.register(ExpenseType)
class ExpenseTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_on', 'modified_on')
    search_fields = ('name',)


@admin.register(Expenditure)
class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ('expenses_type', 'item', 'lrd_amount', 'usd_amount', 'created_by', 'created_on', 'modified_on')
    search_fields = ('item',)
    list_filter = ('expenses_type', 'created_by')
