from django.contrib import admin
from .models import Song

# Register your models here.
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('artist', 'title','song_content','created_by','created_on','modified_on')
    search_fields = ('artist', 'title')
    list_filter = ('artist', 'title')
