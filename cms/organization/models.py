from django.db import models
from django.contrib.auth.models import User
from custom_user.models import CustomUser
from validator.views import valid_phone_number, validate_file_size
from choice.views import status_choices

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    email = models.EmailField(max_length=100, unique=True)
    contact = models.CharField(max_length=150, verbose_name='contact person')
    phone1 = models.CharField(max_length=15, validators=[valid_phone_number], verbose_name='Prim. Phone')
    phone2 = models.CharField(max_length=15, validators=[valid_phone_number], blank=True, null=True, verbose_name='Sec. Phone')
    logo_url = models.FileField(upload_to='organizations', max_length=256, blank=True, null=True, verbose_name="Logo", validators=[validate_file_size])
    status = models.CharField(max_length=100, choices = status_choices, default='active')
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    @property
    def get_contact_person(self):
        return self.contact
