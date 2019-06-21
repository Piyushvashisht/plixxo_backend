from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=60, unique=True)  
    address = models.CharField(max_length=200, unique=True)
    tier = models.PositiveIntegerField()
    icon_id = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name