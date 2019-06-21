from rest_framework import status
from rest_framework.test import APITestCase
from Platform.models import Platform

class PlatformTests(APITestCase):
    def test_create_platform(self):
        url = '/platform/'
        data = {
            'name': 'Insta', 
            'url': 'insta.com',
            'icon_id': 'lookup.com/cool-image-link'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Platform.objects.count(), 1)
        self.assertEqual(Platform.objects.get().name, 'Insta')
        