from django.contrib import admin
from .models import Menu, Orders, Payment

# Register your models here.
admin.site.register(Menu)
admin.site.register(Orders)
admin.site.register(Payment)
