# Generated by Django 3.2.5 on 2021-07-27 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='abc', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
