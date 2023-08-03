from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

class User(AbstractUser):
    def save(self, *args, **kwargs):
        if not self.pk:
            return super().save(*args, **kwargs)
        
class AccumulatedTime(models.Model):
    component=models.CharField(max_length=100,blank=True,default=None)
    component_name=models.CharField(max_length=100,blank=True,default=None)
    component_id=models.CharField(max_length=100,blank=True)
    timestamp = models.DateTimeField(blank=True)
    name = models.CharField(max_length=100,blank=True)
    sequence = models.IntegerField(blank=True)
    subType = models.CharField(max_length=100,blank=True)
    value = models.IntegerField(blank=True)
    def save(self, *args, **kwargs):
        super(AccumulatedTime,self).save(*args,**kwargs)
    def __str__(self):
        return self.name
class Temperature(models.Model):
    composition_id = models.CharField(max_length=100,blank=True)
    timestamp = models.DateTimeField(blank=True)
    sequence = models.IntegerField(blank=True)
    value = models.FloatField(blank=True)
    def save(self, *args, **kwargs):
        super(Temperature,self).save(*args,**kwargs)
    def __str__(self):
        return self.name

class AxisFeedrate(models.Model):
    component=models.CharField(max_length=100,blank=True,default=None)
    component_name=models.CharField(max_length=100,blank=True)
    component_id=models.CharField(max_length=100,blank=True)
    timestamp = models.DateTimeField(blank=True)
    name = models.CharField(max_length=100,blank=True)
    sequence = models.IntegerField(blank=True)
    value = models.FloatField(blank=True)
    def save(self, *args, **kwargs):
        super(AxisFeedrate,self).save(*args,**kwargs)
    def __str__(self):
        return self.name
class AxisFeedrate2(models.Model):
    component=models.CharField(max_length=100,blank=True,default=None)
    component_name=models.CharField(max_length=100,blank=True)
    component_id=models.CharField(max_length=100,blank=True)
    timestamp = models.DateTimeField(blank=True)
    dataItemId = models.CharField(max_length=100,blank=True)
    sequence = models.IntegerField(blank=True)
    value = models.FloatField(blank=True)
    def save(self, *args, **kwargs):
        super(AxisFeedrate2,self).save(*args,**kwargs)
    def __str__(self):
        return self.name

class Position(models.Model):
    component=models.CharField(max_length=100,blank=True,default=None)
    component_name=models.CharField(max_length=100,blank=True)
    component_id=models.CharField(max_length=100,blank=True)
    timestamp = models.DateTimeField(blank=True)
    name = models.CharField(max_length=100,blank=True)
    sequence = models.IntegerField(blank=True)
    subType = models.CharField(max_length=100,blank=True)
    value = models.FloatField(blank=True)
    def save(self, *args, **kwargs):
        super(Position,self).save(*args,**kwargs)
    def __str__(self):
        return self.name
# Create your models here.
