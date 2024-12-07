from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Member
from django.contrib.auth.models import User

# Register your models here.
# class CustomUserAdmin(UserAdmin):
#     def save_model(self, request, obj, form, change):
#         super().save_model(request, obj, form, change)
#         if not change:  # New user creation
#             member = Member.objects.filter(user=obj).first()
#             if member:
#                 member.created_by = request.user
#                 member.save()


# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 
                    'email', 'gender', 'dob','address','nationality', 'phone1', 'phone2','photo_url')
    list_filter = ('status','gender')
    search_fields = ('user__first_name','user__last_name',   'user__email', 'gender', 'nationality', 'phone1', 'phone2', 'address')
    readonly_fields = ('created_by','created_on', 'modified_on')