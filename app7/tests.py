from django.test import TestCase, Client
from django.urls import resolve


# Create your tests here.
class Story7Test(TestCase):
    def test_url_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code,200)