from django.db import models

# Create your models here.


class Car(models.Model):

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    availability = models.BooleanField()
    rent = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
