from django.contrib import admin
from .models import Organization

# Register your models here.
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'email', 'contact', 'phone1', 'phone2', 'logo_url', 'status')
    list_filter = ('address',)
    search_fields =('name', 'address', 'email', 'contact', 'phone1', 'phone2')
