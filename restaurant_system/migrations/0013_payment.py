# Generated by Django 3.0.3 on 2020-05-01 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant_system', '0012_auto_20200501_0647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('card', 'card'), ('cash', 'cash'), ('mobilemoney', 'mobilemoney')], default='cash', max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('payment_amount', models.DecimalField(decimal_places=5, max_digits=10)),
                ('amount', models.FloatField(default=0.0)),
                ('order', models.ManyToManyField(to='restaurant_system.Orders')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
