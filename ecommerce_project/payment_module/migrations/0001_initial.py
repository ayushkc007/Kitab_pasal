# Generated by Django 3.2 on 2021-04-11 04:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_module', '0002_product_isbn'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField()),
                ('city', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('payment_date', models.DateTimeField()),
                ('total_amount', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentGateway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('expiry_date', models.DateField()),
                ('balance', models.FloatField()),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('sub_amount', models.FloatField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment_module.invoice')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.product')),
            ],
        ),
    ]
