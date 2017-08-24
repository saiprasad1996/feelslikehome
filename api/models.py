from django.db import models


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3,primary_key=True)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=100,primary_key=True)
    profile = models.TextField(default='')
    accesstoken = models.TextField(default='')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + "|" + self.email


class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    image = models.ImageField(upload_to="images/stores/")
    address = models.TextField(default="")
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=30,default="")
    longitude = models.CharField(max_length=30,default="")
    categories = models.TextField(default="")

    def __str__(self):
        return self.name



class Reviews(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(default='')
    rating = models.IntegerField()

    def __str__(self):
        return self.review
