from django.db import models
from django.contrib.auth.models import User
from custom_user.models import CustomUser
from member.models import Member
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from datetime import date

# Create your models here.
class MemberDue(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)])
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)])
    date_paid = models.DateField()
    balance = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)], blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.CASCADE, related_name='due_created')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        if self.member.middle_name:
            return '{} {} {}'.format(self.member.first_name, self.member.middle_name, self.member.last_name)
        else:
            return '{} {}'.format(self.member.first_name, self.member.last_name)
    

    def save(self,*args, **kwargs):
        self.balance = self.amount_due - self.amount_paid
        super().save(*args, **kwargs)

    def clean(self):
        super().clean()
        current_date = date.today()
        if self.date_paid > current_date:
            raise ValidationError('Payment date cannot be in the future')
    
   
