from django.db import models

# Create your models here.

class Dict(models.Model):
    
    englishWord = models.CharField(max_length=100)
    rush = models.CharField(max_length=100)

    def __str__(self):
        return self.englishWord