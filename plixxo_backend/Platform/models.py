from django.db import models

class Platform(models.Model):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=100)
    icon_id = models.CharField(max_length=200, unique=True)
    

    def __str__(self):
        return self.name