from django.db import models
from Campaign_content.models import Campaign_content
from User.models import User

class Deliverable(models.Model):
   STATUS_CHOICES = (('Pending','Pending'),
                     ('Accepted','Accepted'),
                     ('Rejected','Rejected'),
                     )
   user_id = models.ForeignKey(User, on_delete=models.CASCADE)
   content_id = models.ForeignKey(Campaign_content, on_delete=models.CASCADE)
   attachment_id = models.CharField(max_length=100)
   meta_data = models.CharField(max_length=200)
   title = models.CharField(max_length=100)
   agency_status = models.CharField(max_length=10,choices=STATUS_CHOICES)
   is_draft = models.BooleanField()
   media_url = models.URLField()
   reject_reason = models.CharField(max_length=200)
   brand_status = models.CharField(max_length=10,choices=STATUS_CHOICES)
    
   def __str__(self):
      return self.title