from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_fname = models.CharField(max_length=30)
    customer_lname = models.CharField(max_length=30)
    customer_email = models.CharField(max_length=50)
class Menu(models.Model):
    UNAVAILABLE = 'unavailable'
    AVAILABLE = 'available'
    CHOICES = (
        (UNAVAILABLE, 'available'),
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
    order_number= models.CharField(max_length=30)
    order_decription= models.CharField(max_length=200)
    order_amount = models.DecimalField(max_digits=10, decimal_places=5)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

class MenueOrder(models.Model):
    menu_id= models.ForeignKey(Menu, on_delete=models.CASCADE)
    order_id= models.ForeignKey(Orders, on_delete=models.CASCADE) 

class PaymentOrder(models.Model):
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
    order_id= models.ForeignKey(Orders, on_delete=models.CASCADE) 

