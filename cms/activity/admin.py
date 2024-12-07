from django.contrib import admin
from .models import Activity

# Register your models here.
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time', 'description', 'created_by', 'created_on', 'modified_on')
    search_fields = ('name',)
