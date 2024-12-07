from django.contrib import admin
from .models import Announcement

# Register your models here.
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('author','title','message','created_by','created_on','modified_on')
    search_fields = ('author','title')
    list_filter = ('created_on',)
