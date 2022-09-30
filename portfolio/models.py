from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(default='',max_length=100)
    description = models.CharField(default='', max_length=255)
    image = models.ImageField(default='', upload_to='portfolio/images')
    url = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.title
