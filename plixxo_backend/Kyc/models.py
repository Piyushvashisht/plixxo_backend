from django.db import models
from User.models import User

class Kyc(models.Model):
   user_id = models.ForeignKey(User, on_delete=models.CASCADE)
   bank_verification_file_id = models.CharField(max_length=100)
   identity_verification_file_id = models.CharField(max_length=100)
   pancard_verification_file_id = models.CharField(max_length=100)
    

   def __str__(self):
      return self.user_id