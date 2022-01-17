from django.db import models

# Create your models here.

class User(models.Model):
    first_name=models.CharField(null=False, max_length=200)
    last_name=models.CharField(null=False, max_length=200)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email=models.EmailField(null=False)
    phone_number=models.CharField(null=False, max_length=50)
    adress=models.CharField(null=False, max_length=200)


    def __repr__(self):
        return f'Customer: {self.first_name}, Phone number: {self.phone_number}'