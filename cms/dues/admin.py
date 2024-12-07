from django.contrib import admin
from .models import MemberDue

# Register your models here.
@admin.register(MemberDue)
class MemberDueAdmin(admin.ModelAdmin):
    list_display = ('member', 'amount_due', 'amount_paid', 'date_paid', 'balance', 'created_by',
                    'created_on','modified_on')
    search_fields = ('member',)
    list_filter = ('balance', 'created_on')
    readonly_fields =('balance',)
