from django.db import models
from django.contrib.auth.models import User
from custom_user.models import CustomUser
from validator.views import valid_phone_number, validate_file_size

# Create your models here.
class ContentType(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,blank=True, null=True, related_name='content_type_created')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name}"
    

class Content(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='content_type')
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    photo_url = models.FileField(upload_to='images/', max_length=256, verbose_name='upload photo', validators=[validate_file_size])
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='content_creator')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title}"

