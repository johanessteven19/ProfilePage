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
        self.assertEqual(found.func, home)

    def test_inside_html(self):
        response=Client().get('')
        response_content = response.content.decode('utf-8')
        self.assertIn("Hello, how are you today?", response_content)
