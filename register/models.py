from django.db import models

# Create your models here.
class AplivationUser(models.Model):
    username = models.CharField(max_length=100, help_text="User Name")
    password = models.CharField(max_length=20, blank=False, null=False)
    
    