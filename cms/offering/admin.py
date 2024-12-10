from django.contrib import admin
from .models import Offering

# Register your models here.
@admin.register(Offering)

class OfferingAdmin(admin.ModelAdmin):
    list_display = ('id', 'offering_type', 'lrd', 'usd', 'description')
    list_filter = ('offering_type',)
    search_fields = ('offering_type','description')
