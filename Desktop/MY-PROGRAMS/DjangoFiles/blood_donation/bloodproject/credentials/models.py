from django.db import models

# Create your models here.
class registration(models.Model):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    username=models.CharField(max_length=250)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=250)
    confirm_password=models.CharField(max_length=250)

    def __str__(self):
        return self.name



class donation(models.Model):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    gender=models.CharField(max_length=250)
    blood_group = models.CharField(max_length=250)
    email=models.EmailField(max_length=254)
    phone=models.IntegerField()
    disease=models.CharField(max_length=250)
    address=models.TextField(max_length=300)

    class meta:
        ordering=('name',)
        verbose_name='doner'
        verbose_name_plural='doners'


    def __str__(self):
        return self.name

