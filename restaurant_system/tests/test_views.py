from django.test import TestCase, Client 
from django.urls import reverse
from restaurant_system.models import Menu, Orders,Payment
import json 

class TestViews(TestCase):
    def setUp(self):
        client = Client()
        self.menu_url = reverse(getMenu)
    def test_getMenu(self):
        url = reverse
        response = self.client.get(self.menu_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'restaurant_system/menu.html')

