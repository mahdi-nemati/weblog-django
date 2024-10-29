from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    author = models.CharField(max_length=20)
    created_at = models.DateField()