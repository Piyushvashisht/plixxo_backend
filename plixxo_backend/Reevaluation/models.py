from django.db import models
from User.models import User

class Reevaluation(models.Model):
   user_id = models.ForeignKey(User, on_delete=models.CASCADE)
   reevaluated_at = models.DateTimeField()
   reevaluated_by = models.CharField(max_length=50)
    

   def __str__(self):
      return self.id