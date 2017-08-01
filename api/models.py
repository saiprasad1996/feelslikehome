from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    profile = models.TextField(default='')
    country = models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.name+"|"+self.email

class Store(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    image = models.TextField()

    def __str__(self):
        return self.name

class Location(models.Model):
    address = models.TextField()
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    store = models.ForeignKey(Store,on_delete=models.CASCADE)

    def __str__(self):
        return self.address

class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class StoreCategory(models.Model):
    storekey = models.ForeignKey(Store,on_delete=None)
    categorykey = models.ForeignKey(Category,on_delete=None)

class Reviews(models.Model):
    store = models.ForeignKey(Store,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    review = models.TextField(default='')
    rating = models.IntegerField()

    def __str__(self):
        return self.review
