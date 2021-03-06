# Generated by Django 3.2.5 on 2021-07-28 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstoreapp', '0002_rename_books_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='img',
            field=models.ImageField(default='abc', upload_to='gallery'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.CharField(max_length=250),
        ),
    ]
