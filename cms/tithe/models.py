from django.db import models
from member.models import Member
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from custom_user.models import CustomUser
from datetime import date
from django.core.exceptions import ValidationError

# Create your models here.
class Tithe(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='member_tithe')
    usd_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, null=True, blank=True, validators=[MinValueValidator(0.00)])
    lrd_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, null=True, blank=True, validators=[MinValueValidator(0.00)])
    payment_date = models.DateField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        if self.member.middle_name:  
            return '{} {} {}'.format(self.member.first_name, self.member.middle_name, self.member.last_name)
        else:
            return '{} {}'.format(self.member.first_name, self.member.last_name)
    
    
    def clean(self):
        super().clean()
        if self.payment_date > date.today():
            raise ValidationError("Payment date cannot be in the future.")
    
