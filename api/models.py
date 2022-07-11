from tkinter import TRUE
from django.db import models
from django.forms import BooleanField

# Create your models here.
class Category(models.Model):
    Category_id = models.IntegerField(primary_key=TRUE)
    Category_Name = models.CharField(max_length=60)
    Category_Description = models.CharField(max_length=200)
    Category_Image = models.ImageField()
    ACTIVE = 0
    INACTIVE = 1
    STATUS = (
        (ACTIVE,('Active')),
        (INACTIVE,('Inactive')),
    )
    Category_Status =models.IntegerField(default=1,choices=STATUS)
    
class State(models.Model):
    State_id = models.IntegerField(primary_key=TRUE)
    State_Name = models.CharField(max_length=60)
    State_Description = models.CharField(max_length=200)
    State_Image = models.ImageField()

class Zone(models.Model):
    Zone_id = models.IntegerField(primary_key=TRUE)
    Zone_Name = models.CharField(max_length=60)
    Zone_Description = models.CharField(max_length=200)
    Zone_Image = models.ImageField()
    
class PackagesType(models.Model):
    PackagesType_Name = models.CharField(max_length=60)
    PackagesType_Description = models.CharField(max_length=200)
    PackagesType_Image = models.ImageField()
    
class Package(models.Model):
    Package_id = models.IntegerField(primary_key=TRUE)
    Package_Name = models.CharField(max_length=60)
    Package_Description = models.CharField(max_length=200)
    Package_BannerImage = models.ImageField()
    package_Duration = models.TimeField()
    package_Inclusion= models.CharField(max_length=300)
    package_Category_id = models.IntegerField()
    Category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
    State_id = models.ForeignKey(State,on_delete=models.PROTECT)
    Zone_id = models.ForeignKey(Zone,on_delete=models.PROTECT)
    
class Package_Itinerary_items(models.Model):
    Itinerary_items_id = models.IntegerField(primary_key=TRUE)
    Itinerary_items_title = models.CharField(max_length=60)
    DAY_CHOICES = (
        ('1',"Monday"),
        ('2',"Tuesday"),
        ('3',"Wednesday"),
        ('4',"Thursday"),
        ('5',"Friday"),
        ('6',"Saturday"),
        ('7',"Sunday"),
    ) 
    Itinerary_items_Day = models.CharField(max_length=1, choices=DAY_CHOICES)
    Itinerary_items_Image = models.ImageField()
    Itinerary_items_Description = models.CharField(max_length=200)
