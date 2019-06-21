from django.db import models
from Brand.models import Brand

class Campaign(models.Model):
    title = models.CharField(max_length=100)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    campaign_description_id = models.PositiveIntegerField()
    approved_by = models.CharField(max_length=30)
    agency_notes = models.CharField(max_length=100)
    deleted_at = models.DateTimeField()
    start_date = models.DateField()
    end_date = models.DateField()
    pinned = models.BooleanField()
    moderation_url_sharing = models.URLField()
    price = models.FloatField()
    total_slots = models.PositiveIntegerField()
    what_you_get = models.CharField(max_length=30)
    
    def __str__(self):
        return self.title