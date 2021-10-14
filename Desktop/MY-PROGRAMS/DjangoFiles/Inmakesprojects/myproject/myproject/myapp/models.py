from django.db import models

# Create your models here.
class our_services(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class why_choos_us(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()

    def __str__(self):
        return self.name
