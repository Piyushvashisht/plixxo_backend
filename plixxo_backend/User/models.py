from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _ 
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
      username = models.CharField(max_length=30,blank=True, null=True)
      email = models.EmailField(_('email address'), unique=True)

      USERNAME_FIELD = 'email'
      REQUIRED_FIELDS = ['username','first_name']

      def __str__(self):
            return "{}".format(self.email)



class UserProfile(models.Model):

      STATUS_CHOICES = (('Pending','Pending'),
                     ('Approved','Approved'),
                     ('Blacklisted','Blacklisted'),
                     )
      ROLE_CHOICES = (('Brand','Brand'),
                     ('Influencer','Influencer'),
                     ('Agency','Agency'),
                     )
      GENDER_CHOICES = (('Male','Male'),
                     ('Female','Female'),
                     )
      def year_choices():
            return [(r,r) for r in range(1, 6)]

      user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
      gender = models.CharField(max_length=6,choices=GENDER_CHOICES)
      dob = models.DateField()
      mobile_no = PhoneNumberField(unique=True)  
      address = models.CharField(max_length=200, unique=True)
      bio =models.CharField(max_length=250)
      role =  models.CharField(max_length=15,choices=ROLE_CHOICES)
      paytm_no = PhoneNumberField(unique=True)
      referral_code = models.CharField(max_length=16, unique=True)
      status = models.CharField(max_length=15,choices=STATUS_CHOICES)
      college_name = models.CharField(max_length=100,null=True)
      college_year = models.PositiveIntegerField(choices=year_choices(),null=True)
      dp_id = models.CharField(max_length=100, unique=True, null=True)
