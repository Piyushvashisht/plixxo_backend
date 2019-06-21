from rest_framework import status
from rest_framework.test import APITestCase
from User.models import User

class UserTests(APITestCase): 
    def test_create_brand(self):
        url = '/user/'
        data = {
            'first_name': "Pankaj", 
            'last_name': "Yadav", 
            'email': "abcdefgh@gmail.com",
            'address': "Somewhere in the world",
            'gender' : "Male",
            'dob' : "1999-05-06",
            'mobile_no' : "+918802746054",
            'password' : "testing",
            'bio' : "tesing user model",
            'role' : "Influencer",
            'paytm_no' : "+918802746054",
            'referral_code' : "referral",
            'status' : "Coding...",
            'college_name' : "MIT",
            'college_year' : "2",
            'dp_id': 'lookup.com/cool-image-link'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().mobile_no, '+918802746054')
