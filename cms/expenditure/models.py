from django.db import models
from django.contrib.auth.models import User
from custom_user.models import CustomUser
from django.core.validators import MinValueValidator



# Create your models here.
class ExpenseType(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

class Expenditure(models.Model):
    expenses_type = models.ForeignKey(ExpenseType, on_delete=models.CASCADE, related_name="expenses")
    item = models.CharField(max_length=200)
    lrd_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, null=True, blank=True, validators=[MinValueValidator(0.00)])
    usd_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, null=True, blank=True, validators=[MinValueValidator(0.00)])
    description = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.item}"
