# Generated by Django 3.1 on 2020-10-22 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_shoppingaddress_default'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoppingaddress',
            options={'verbose_name_plural': 'Addresses'},
        ),
    ]
