from django.db import models
from Campaign.models import Campaign

class Campaign_content(models.Model):
    campaign_id = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    deleted_at = models.DateField()
    description = models.CharField(max_length=250)
    is_price_fixed = models.BooleanField()
    max_price = models.FloatField()
    fixed_price = models.FloatField()
    min_price = models.FloatField()
    title = models.CharField(max_length=100)
    attachment_id = models.CharField(max_length=200)
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.title