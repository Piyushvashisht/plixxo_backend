from django.db import models
from User.models import User
from Platform.models import Platform

class Media_handles(models.Model):
   user_id = models.ForeignKey(User, on_delete=models.CASCADE)
   platform_id = models.ForeignKey(Platform, on_delete=models.CASCADE)
   handle = models.CharField(max_length=50, unique=True)
   meta_data = models.CharField(max_length=200)
   params = models.CharField(max_length=100)
   access_token = models.CharField(max_length=100,unique=True)
   reset_token = models.CharField(max_length=100)
   token_expiry_date = models.DateField()
   
   def __str__(self):
      return self.handle