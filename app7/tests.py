from django.test import TestCase, Client
from django.urls import resolve

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from .views import home, show
from .models import Data
from .forms import DataForm

import time
# Create your tests here.

class Story7Test(TestCase):
    def test_url_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code,200)
    
    def test_story7_using_home_func(self):
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
        self.assertEqual(response.status_code,200)

    def test_story7_using_show_func(self):
        found = resolve('/show.html')
        self.assertEqual(found.func, show) 

    def test_inside_html2(self):
        response=Client().get('/show.html')
        response_content = response.content.decode('utf-8')
        self.assertIn("See how the world is feeling today.", response_content)


## -------- Functional Test ---------
class Story7FunctionalTest(TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--dns-prefetch-disable')
        chrome_options.add_argument('--no-sandbox')        
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('disable-gpu')
        self.selenium  = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
        super(Story7FunctionalTest, self).setUp()


    def tearDown(self):
        self.selenium.quit()
        super(Story7FunctionalTest, self).tearDown()

    def test_input_todo(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('https://story7jo.herokuapp.com/')
        # selenium.get('localhost:8000')
        # find the form element
        selenium.implicitly_wait(1)

        name = selenium.find_element_by_name('name')
        status = selenium.find_element_by_name('status')

        name.send_keys("namates")
        status.send_keys('hello')
        submit = selenium.find_element_by_id('statussubmit')
        submit.click()

        view = selenium.find_element_by_id('viewbtn')
        view.click()
        selenium.get('https://story7jo.herokuapp.com/show.html')
        time.sleep(7)   