# Generated by Django 3.2 on 2021-05-06 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0003_alter_product_isbn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('best_seller_productID', models.IntegerField()),
                ('our_pick_productID', models.IntegerField()),
                ('new_arrival_productID', models.IntegerField()),
            ],
        ),
    ]
