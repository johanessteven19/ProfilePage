from django.test import TestCase, Client
from django.urls import resolve

from .views import home, show
from .models import Data
from .forms import DataForm

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

    def test_model_can_create_new_data(self):
        Data.objects.create(name='namates', status='halo')
        data_count = Data.objects.all().count()
        self.assertEqual(data_count, 1)

    def test_form_validation_for_blank_items(self):
        form = DataForm(data={'name':'','status':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['name'],
            ["This field is required."]
        )
        self.assertEqual(
            form.errors['status'],
            ["This field is required."]
        )

    def test_story_using_show_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'index.html')

    def test_url2_exist(self):
        response = Client().get('/show.html')
        self.assertEqual(response.status_code,302)

