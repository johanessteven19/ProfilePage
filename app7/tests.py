from django.test import TestCase, Client
from django.urls import resolve
from .views import home

# Create your tests here.
class Story7Test(TestCase):
    def test_url_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code,200)
    
    def test_story7_using_index_func(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

