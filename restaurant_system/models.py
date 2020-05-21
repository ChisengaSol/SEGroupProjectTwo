from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth import get_user_model
User = get_user_model()


# class User(AbstractUser):
#     username = models.CharField(max_length=50, blank=True, null=True)
#     email = models.EmailField(_('email address'), unique=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

#     def __str__(self):
#         return "{}".format(self.email)

# Create your models here.
class Customer(models.Model):
    customer_fname = models.CharField(max_length=30)
    customer_lname = models.CharField(max_length=30)
    customer_email = models.CharField(max_length=50)
class Menu(models.Model):
    UNAVAILABLE = 'unavailable'
    AVAILABLE = 'available'
    BREAKFAST = 'breakfast'
    LUNCH = 'lunch'
    DINNER= 'dinner'
    DRINKS= 'drinks'

    CHOICES = (
        (UNAVAILABLE, 'unavailable'),
        (AVAILABLE , 'available'),
    )

    CATEGORIES=(
        (BREAKFAST, 'breakfast'),
        (LUNCH, 'lunch'),
        (DINNER, 'dinner'),
        (DRINKS, 'drinks')
    )

    meal_name = models.CharField(max_length=30)
    meal_price = models.DecimalField(max_digits=10, decimal_places=5)
    meal_image = models.ImageField(upload_to='uploads/')
    meal_availability_status = models.CharField(max_length=255, choices=CHOICES, default=AVAILABLE)
    meal_category = models.CharField(max_length=30, choices=CATEGORIES, default=LUNCH)



class Orders(models.Model):
    DRAFT = 'draft'
    CONFIRMED = 'confirmed'
    DECLINED = 'declined'
    CHOICES = (
        (DRAFT, 'draft'), 
        (CONFIRMED , 'confirmed'),
        (DECLINED, 'declined'),
    )
    menu = models.ManyToManyField(Menu)   
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    order_status = models.CharField(max_length=255, choices=CHOICES, default=DRAFT)

class Payment(models.Model):
    CARD = 'card'
    CASH = 'cash'
    MOBILEMONEY = 'mobilemoney'
    MOBILEMONEY = 'mobilemoney'
    CHOICES = (
        (CARD, 'card'), 
        (CASH , 'cash'),
        (MOBILEMONEY, 'mobilemoney'),
    )
    payment_method = models.CharField(max_length=255, choices=CHOICES, default=CASH)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    payment_amount= models.DecimalField(max_digits=10, decimal_places=5)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order = models.ManyToManyField(Orders)
    amount = models.FloatField(default=0.0)
# class PaymentOrder(models.Model):
#     payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
