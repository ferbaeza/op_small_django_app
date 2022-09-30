from django.db import models
import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(default='',max_length=100)
    body = models.TextField(default='')
    image = models.ImageField(upload_to = 'images')
    date = models.DateField(default=datetime.date.today)

    def __str__(self) -> str:
        return self.title


