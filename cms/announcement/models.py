from django.db import models
from django.contrib.auth.models import User
from custom_user.models import CustomUser


# Create your models here.
class Announcement(models.Model):
    author = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200)
    message = models.TextField()
    created_by = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.CASCADE, related_name='announcement_created')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '{} {}'.format(self.author, self.title)


