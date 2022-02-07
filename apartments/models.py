from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Apartment(models.Model):

    name = models.CharField(max_length=200)
    sale = models.BooleanField()
    rent = models.BooleanField()
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.EmailField()
    activated = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Name {self.name}'


class Owner(models.Model):
    name = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    owner = models.CharField(max_length=200)
    workers = models.PositiveIntegerField()
    workers_number = models.PositiveIntegerField(blank=True)
    email = models.TextField()

    def save(self,*args, **kwargs):
        self.workers_number = self.workers
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Owner: {self.owner} / Number of workers: {self.workers_number}'

