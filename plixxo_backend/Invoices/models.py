from django.db import models
from User.models import User

class Invoices(models.Model):
   STATUS_CHOICES = (('Pending', 'Pending'),
                     ('Cleared', 'Cleared'),
                     ('Rejected', 'Rejected'),
                     ('Deleted', 'Deleted'),
                     )
   user_id = models.ForeignKey(User, on_delete=models.CASCADE)
   amount = models.PositiveIntegerField()
   tax = models.FloatField()
   raised_at = models.DateTimeField()
   cleared_at = models.DateTimeField()
   deleted_at = models.DateTimeField()
   status = models.CharField(max_length=10, choices=STATUS_CHOICES)
   rejected_by = models.CharField(max_length=30)
   rejection_reason = models.CharField(max_length=100)

   def __str__(self):
      return self.id
