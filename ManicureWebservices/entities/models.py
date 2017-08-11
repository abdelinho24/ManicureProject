from django.core.validators import RegexValidator
from django.db import models

# Create your models here.


class User(models.Model):
        firstname = models.CharField(max_length=255, null=False)
        lastname = models.CharField(max_length=255, null=False)
        phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
        phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True)# validators should be a list
        type = models.CharField(max_length=255, null=False)
        date_of_birth = models.DateTimeField(max_length=255, blank=True, null=True)
        sex = models.CharField(max_length=2)
        address = models.CharField(max_length=255)
        rate = models.IntegerField()
        email = models.EmailField(null=True)


class Service(models.Model):
        name = models.CharField(max_length=255)
        category = models.CharField(max_length=255)
        duration = models.DurationField(blank=True)
        price = models.DecimalField(max_digits=8, decimal_places=2)


class Appointment(models.Model):
        name = models.CharField(max_length=255)
        date = models.DateTimeField(max_length=255, blank=True, null=True)
        pro = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pro")
        customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer")