from django.db import models
from User.models import User
from Campaign.models import Campaign


class Proposal(models.Model):
   STATUS_CHOICES = (('Sent','Sent'),
                     ('Pending','Pending'),
                     ('Accepted','Accepted'),
                     ('Rejected','Rejected'),
                     )
   user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   campaign_id = models.ForeignKey(Campaign,on_delete=models.CASCADE, null=True)
   status = models.CharField(max_length=10,choices=STATUS_CHOICES,null=True)

   def __str__(self):
      return self.id