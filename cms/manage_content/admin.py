from django.contrib import admin
from .models import Content,ContentType
# Register your models here.
@admin.register(ContentType)
class ContentTypeAdmin(admin.ModelAdmin):
    list_display = ('name','created_by','created_on','modified_on')
    search_fields = ('name',)

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('content_type','title','description','photo_url','created_by','created_on','modified_on')
    search_fields = ('content_type', 'title')
    list_filter = ('content_type',)

