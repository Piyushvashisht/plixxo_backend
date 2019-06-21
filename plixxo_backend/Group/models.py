from django.db import models
from User.models import User

class Group(models.Model):
   user_id = models.ForeignKey(User, on_delete=models.CASCADE)
   group_name = models.CharField(max_length=50)


   def __str__(self):
      return self.group_name