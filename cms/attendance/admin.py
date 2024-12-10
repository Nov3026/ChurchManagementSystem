from django.contrib import admin
from .models import ChoirAttendance, ChurchServiceAttendance

# Register your models here.
admin.register(ChurchServiceAttendance)

@admin.register(ChoirAttendance)
class ChoirAttendanceAdmin(admin.ModelAdmin):
    list_display = ('member','activity','day','status','created_by','created_on','modified_on')
    search_fields = ('member__first_name','member__last_name')
    list_filter = ('activity','status')

