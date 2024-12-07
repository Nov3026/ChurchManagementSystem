from django.db import models
from django.contrib.auth.models import Group
from organization.models import Organization

# Extend the Group model with a OneToOne relationship or ForeignKey to Organization
class GroupExtension(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.group.name} - {self.organization.name}"