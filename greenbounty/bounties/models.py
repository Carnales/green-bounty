from django.db import models
from django.contrib.auth.models import User

#user, bounty, organizations

class Hunter(models.Model):
    #include: user, name
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Bounty(models.Model):
    #include: name, city, price, usersname, image
    hunter = models.ForeignKey(Hunter, on_delete=models.SET_NULL, blank=True, null=True)

    name = models.CharField(max_length=25, null=True)
    image = models.ImageField(null=True, blank=True)
    price = models.FloatField()
    city = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.name

class Organization(models.Model):
    #include: name, balance, total_contributions
    name = models.CharField(max_length=25, null=True)
    balance = models.FloatField()
    total = models.FloatField()

