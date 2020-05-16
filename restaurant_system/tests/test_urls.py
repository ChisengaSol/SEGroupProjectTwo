from django.test import SimpleTestCase
from django.urls import reverse, resolve
from restaurant_system.views import getMenu, Orderform, makeMoreOrders, paymentconfirmation
class TestUrls(SimpleTestCase):
    def test_getMenuUrl(self):
        url = reverse(getMenu)
        self.assertEquals(resolve(url).func,getMenu)
    def test_OrderFormUrl(self):
        url = reverse(Orderform)
        self.assertEquals(resolve(url).func,Orderform)
    def test_makeMoreOrdersUrl(self):
        url = reverse(makeMoreOrders)
        self.assertEquals(resolve(url).func,makeMoreOrders)
    def test_paymentconfirmationUrl(self):
        url = reverse(paymentconfirmation)
        self.assertEquals(resolve(url).func,paymentconfirmation)



