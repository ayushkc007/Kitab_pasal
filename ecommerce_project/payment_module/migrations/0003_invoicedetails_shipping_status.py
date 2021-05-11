# Generated by Django 3.2 on 2021-05-10 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_module', '0002_invoice_contact_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicedetails',
            name='shipping_status',
            field=models.CharField(choices=[('confirmed', 'confirmed'), ('shipping', 'shipping'), ('received', 'received')], default=1, max_length=256),
            preserve_default=False,
        ),
    ]
