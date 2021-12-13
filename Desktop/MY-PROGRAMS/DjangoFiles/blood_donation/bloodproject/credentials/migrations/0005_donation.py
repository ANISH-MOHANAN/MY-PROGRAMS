# Generated by Django 3.2.9 on 2021-12-13 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0004_delete_donation'),
    ]

    operations = [
        migrations.CreateModel(
            name='donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('gender', models.CharField(max_length=250)),
                ('blood_group', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('disease', models.CharField(max_length=250)),
                ('address', models.TextField(max_length=300)),
            ],
        ),
    ]
