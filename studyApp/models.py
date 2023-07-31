from django.db import models

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField(default='')
    image_path = models.TextField(default='')
    is_legal = models.BooleanField(default=True)

class Meta:
        app_label = 'studyApp'