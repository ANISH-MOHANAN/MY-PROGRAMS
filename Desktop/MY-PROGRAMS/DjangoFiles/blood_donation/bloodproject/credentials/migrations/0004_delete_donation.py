# Generated by Django 3.2.9 on 2021-12-11 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0003_donation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='donation',
        ),
    ]