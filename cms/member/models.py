from django.db import models
from django.contrib.auth.models import  Group
from custom_user.models import CustomUser
from choice.views import member_status_choices, gender_choices
from validator.views import valid_phone_number, validate_file_size
from django_countries.fields import CountryField
from datetime import date
from django.core.exceptions import ValidationError

# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name='username', related_name='member_user')
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100, unique=True)
    gender = models.CharField(max_length=10, choices=gender_choices)
    dob = models.DateField(verbose_name='date of birth', blank=True, null=True)
    address = models.CharField(max_length=250)
    nationality = CountryField(blank=('selected country'))
    phone1 = models.CharField(max_length=15, validators=[valid_phone_number], verbose_name='Prim. Phone')
    phone2 = models.CharField(max_length=15, validators=[valid_phone_number], blank=True, null=True, verbose_name='Sec. Phone')
    address = models.TextField(max_length=250)
    photo_url = models.FileField(upload_to='members', max_length=256, verbose_name='profile photo', validators=[validate_file_size], blank=True, null=True)
    status = models.CharField(max_length=25, choices=member_status_choices, default='active')
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='member_created', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        if self.middle_name:
            return '{} {} {}'.format(self.first_name, self.middle_name, self.last_name)
        else:
            return '{} {}'.format(self.first_name, self.last_name)
    
    def clean(self):
        super().clean()
        if self.dob > date.today():
                raise ValidationError("Date of Birth cannot be in the future")
        

    @classmethod
    def add_user_to_group(cls, new_user, group_name):
        my_group = Group.objects.get(name=group_name.upper())
        new_user.groups.add(my_group)






