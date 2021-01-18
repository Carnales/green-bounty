from django.db import models
from django.contrib.auth.models import User

#user, bounty, organizations

class Hunter(models.Model):
    #include: user, name
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=True)
    image = models.ImageField(null=True, blank=True)
    bounties = models.FloatField(default=0)
    points = models.FloatField(default=0)
    balance = models.FloatField(default=0)

    def __str__(self):
        return self.name

    @property
    def profile_pic(self):
        try:
            img = self.image.url
        except Exception as e:
            img = ''
        return img

class Bounty(models.Model):
    #include: name, city, price, usersname, image
    hunter = models.ForeignKey(Hunter, on_delete=models.SET_NULL, blank=True, null=True)

    image = models.ImageField(null=True, blank=True)
    price = models.FloatField()
    city = models.CharField(max_length=25, null=True)
    location = models.CharField(max_length=25, null=True)

    @property
    def imageURL(self):
        try:
            img = self.image.url
        except Exception as e:
            img = ''
        return img

    @property
    def username(self):
        return self.hunter.name

class Organization(models.Model):
    #include: name, balance, total_contributions
    name = models.CharField(max_length=25, null=True)
    balance = models.FloatField()

    def __str__(self):
        return self.name

    @property
    def total_contributions(self):
        transactions = self.transaction_set.all()
        total = sum([transaction.price for transaction in transactions])
        return total

class Transaction(models.Model):
    #include: price, organization
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, blank=True, null=True)
    price = models.FloatField()

class Submission(models.Model):
    #include: price, organization
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(max_length=200, null=True)

