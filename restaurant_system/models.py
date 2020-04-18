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
    CHOICES = (
<<<<<<< HEAD
        (UNAVAILABLE, 'unavailable'),
=======
        (UNAVAILABLE, 'available'),
>>>>>>> 0b15ddb706505c912b47b7b9263961612c8d20bf
        (AVAILABLE , 'available'),
    )

    meal_name = models.CharField(max_length=30)
    meal_price = models.DecimalField(max_digits=10, decimal_places=5)
    meal_image = models.ImageField(upload_to='uploads/')
    meal_availability_status = models.CharField(max_length=255, choices=CHOICES, default=AVAILABLE)

class Payment(models.Model):
    payment_type = models.CharField(max_length=30)
    payment_date = models.CharField(max_length=30)
    payment_amount= models.DecimalField(max_digits=10, decimal_places=5)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

class Orders(models.Model):
    menu = models.ManyToManyField(Menu)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

<<<<<<< HEAD
=======

>>>>>>> 0b15ddb706505c912b47b7b9263961612c8d20bf
class PaymentOrder(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)

