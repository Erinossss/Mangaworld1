# Generated by Django 3.1 on 2020-09-28 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='release',
            field=models.DateTimeField(),
        ),
    ]
