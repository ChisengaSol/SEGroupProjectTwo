# Generated by Django 3.0.3 on 2020-04-29 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_system', '0010_orders_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_status',
            field=models.CharField(choices=[('draft', 'draft'), ('confirmed', 'confirmed'), ('declined', 'declined')], default='draft', max_length=255),
        ),
    ]
