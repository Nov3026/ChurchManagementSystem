from django.contrib import admin
from .models import Tithe

# Register your models here.
@admin.register(Tithe)
class TitheAdmin(admin.ModelAdmin):
    list_display = ('member', 'lrd_amount','usd_amount','payment_date', 'created_by','created_on','modified_on')
    search_fields =('member_first_name','member_last_name')
    list_filter =('lrd_amount','usd_amount','payment_date')
