from rest_framework import status
from rest_framework.test import APITestCase
from Brand.models import Brand

class BrandTests(APITestCase): 
    def test_create_brand(self):
        url = '/brand/'
        data = {
            'name': "Holy Marijo", 
            'email': "holygavkamole@gmail.com",
            'address': "Plixxo HQ",
            'tier': 1,
            'icon_id': 'lookup.com/cool-image-link'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Brand.objects.count(), 1)
        self.assertEqual(Brand.objects.get().name, 'Holy Marijo')
