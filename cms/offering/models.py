from django.db import models
from custom_user.models import CustomUser
from choice.views import offering_choices
from django.core.validators import MinValueValidator

# Create your models here.
class Offering(models.Model):
    offering_type = models.CharField(max_length=20, choices=offering_choices)
    lrd = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)])
    usd = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)])
    description = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.offering_type}"

