from django.db import models
from choice.views import  days_choices, choir_attendance_status_choices
from activity.models import Activity
from django.contrib.auth.models import User
from custom_user.models import CustomUser
from member.models import Member


# Create your models here.
class ChurchServiceAttendance(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='church_activity') 
    men = models.IntegerField(null=True, blank=True, verbose_name='total mem')
    women = models.IntegerField(null=True, blank=True, verbose_name='total women')
    children1 = models.IntegerField(null=True, blank=True, verbose_name='total male children')
    children2 = models.IntegerField(null=True, blank=True, verbose_name='total female children')
    vistor = models.IntegerField(null=True, blank=True)
    total_attendees = models.IntegerField(null=True, blank=True)
    created_by = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.CASCADE, related_name='attendance_created')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.activity}"
    
    def save(self, *args, **kwargs):
        self.total_attendees = self.men + self.women + self.children1 + self.children2 + self.vistor
        super().save(*args, **kwargs)

    class Meta:
        ordering =['-created_on']
 

class ChoirAttendance(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='choir_member')
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='activity')
    day = models.CharField(max_length=20, choices=days_choices, default=None)
    status = models.CharField(max_length=20, choices=choir_attendance_status_choices, default='present')
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='choir_attendance', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '{} {} {}'.format(self.member.first_name, self.member.middle_name, self.member.last_name)
    
    class Meta:
        ordering = ['-created_on']
    
    