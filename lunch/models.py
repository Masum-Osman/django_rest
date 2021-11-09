from django.db import models
from django.db.models.fields import DateField

# Create your models here.

class Restaurants(models.Model):
    restaurantId = models.AutoField(primary_key=True)
    restaurantName = models.CharField(max_length=220)
    ownerName = models.CharField(max_length=220)
    createdOn = models.DateField()


class Employees(models.Model):
    employeeId = models.AutoField(primary_key=True)
    employeeName = models.CharField(max_length=220)
    department = models.CharField(max_length=220)
    dateOfJoining = models.DateField()


class Menu(models.Model):
    menuId = models.AutoField(primary_key=True)
    restaurantId = models.IntegerField(11)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    summery = models.CharField(max_length=200)
    price = models.FloatField(11)
    createdOn = models.DateField()


class Vote(models.Model):
    voteId = models.AutoField(primary_key=True)
    employeeId = models.IntegerField(11)
    menuId = models.IntegerField(11)
    votedOn = models.DateField()
