from django.db import models
from custom_user.models import CustomUser


# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=200)
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.CharField(max_length=250, blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,blank=True, null=True, related_name='activity_created')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name}"
    

