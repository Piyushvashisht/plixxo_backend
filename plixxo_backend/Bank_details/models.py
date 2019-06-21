from django.db import models
from User.models import User

class Bank_details(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=50)
    account_holder_name = models.CharField(max_length=50)
    account_no = models.CharField(max_length=20,unique=True)  
    address = models.CharField(max_length=200, unique=True)
    city = models.CharField(max_length=30)
    pincode = models.PositiveIntegerField()
    country = models.CharField(max_length=30)
    details_verification = models.CharField(max_length=50)
    gst_no = models.CharField(max_length=50,unique=True)
    gst_sac_code = models.CharField(max_length=50)
    gst_service_description = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=50)
    gst_service_description = models.CharField(max_length=50)
    gst_registered = models.BooleanField()
    pancard = models.CharField(max_length=20,unique=True)
    service_tax_applicable = models.FloatField()


