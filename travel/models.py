from django.db import models

# Create your models here.

class Travel(models.Model):
    name = models.CharField(max_length=30)
    imgs = models.ImageField(upload_to='mypic')
    description = models.TextField()
    
    def __str__(self):
        return self.name