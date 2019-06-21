from django.db import models
from User.models import User

class User_tags(models.Model):
   user_id = models.ForeignKey(User, on_delete=models.CASCADE)
   tags = models.CharField(max_length=150)
    


   def __str__(self):
      return self.tags