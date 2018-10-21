# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TblCar(models.Model):
    id_clients = models.IntegerField(db_column='id_Clients')  # Field name made lowercase.
    id_car = models.CharField(db_column='id_Car', primary_key=True, max_length=11)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=30)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=30)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200)  # Field name made lowercase.
    specialservices = models.IntegerField(db_column='SpecialServices')  # Field name made lowercase.
    automatic = models.IntegerField(db_column='Automatic')  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    ac = models.IntegerField(db_column='AC')  # Field name made lowercase.
    doors = models.IntegerField(db_column='Doors')  # Field name made lowercase.
    turbo = models.IntegerField(db_column='Turbo')  # Field name made lowercase.
    passagers = models.IntegerField(db_column='Passagers')  # Field name made lowercase.
    numsuitcase = models.IntegerField(db_column='NumSuitCase')  # Field name made lowercase.
    kmxl = models.IntegerField(db_column='KMxL')  # Field name made lowercase.
    airbags = models.IntegerField(db_column='AirBags')  # Field name made lowercase.
    abs = models.IntegerField(db_column='ABS')  # Field name made lowercase.
    costxday = models.FloatField(db_column='CostxDay')  # Field name made lowercase.
    averagecost = models.FloatField(db_column='AverageCost')  # Field name made lowercase.
    babysit = models.IntegerField(db_column='BabySit')  # Field name made lowercase.
    childsit = models.IntegerField(db_column='ChildSit')  # Field name made lowercase.
    gps = models.IntegerField(db_column='GPS')  # Field name made lowercase.
    agerestriction = models.IntegerField(db_column='AgeRestriction')  # Field name made lowercase.
    latepolicy = models.IntegerField(db_column='LatePolicy')  # Field name made lowercase.
    rentalrestrictions = models.IntegerField(db_column='RentalRestrictions')  # Field name made lowercase.
    smokerestriction = models.IntegerField(db_column='SmokeRestriction')  # Field name made lowercase.
    audiobluetooth = models.IntegerField(db_column='AudioBluetooth')  # Field name made lowercase.
    audioaux = models.IntegerField(db_column='AudioAux')  # Field name made lowercase.
    customaudio = models.IntegerField(db_column='CustomAudio')  # Field name made lowercase.
    number_4x4 = models.IntegerField(db_column='4x4')  # Field renamed because it wasn't a valid Python identifier.
    sparetier = models.IntegerField(db_column='SpareTier')  # Field name made lowercase.
    alarm = models.IntegerField(db_column='Alarm')  # Field name made lowercase.
    sensor = models.IntegerField(db_column='Sensor')  # Field name made lowercase.
    travelout = models.IntegerField(db_column='travelOut')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_car'





class RelationsCarimages(models.Model):
    id_car = models.IntegerField(db_column='id_Car')  # Field name made lowercase.
    urlimg = models.CharField(db_column='UrlImg', max_length=100)  # Field name made lowercase.
    file = models.FileField(upload_to='C:/Users/David Sandoval/Desktop/API/RaeBe/Files/car-images')

    class Meta:
        managed = False
        db_table = 'relations_carimages'


class TblPolicy(models.Model):
    id_policy = models.AutoField(db_column='id_Policy', primary_key=True)  # Field name made lowercase.
    id_car = models.CharField(db_column='id_Car', max_length=11)  # Field name made lowercase.
    clientpolicynumber = models.IntegerField(db_column='ClientPolicyNumber')  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=50)  # Field name made lowercase.
    clientpolicyname = models.CharField(db_column='ClientPolicyName', max_length=50)  # Field name made lowercase.
    validationdatestart = models.DateField(db_column='ValidationDateStart')  # Field name made lowercase.
    validationdateend = models.DateField(db_column='ValidationDateEnd')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_policy'




class RelationsCoverage(models.Model):
    id_coverage = models.AutoField(db_column='id_Coverage', primary_key=True)  # Field name made lowercase.
    id_policy = models.IntegerField(db_column='id_Policy')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50)  # Field name made lowercase.
    assurancesum = models.CharField(db_column='AssuranceSum', max_length=50)  # Field name made lowercase.
    deductibles = models.FloatField(db_column='Deductibles')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relations_coverage'

class File(models.Model):
  file = models.FileField(blank=False, null=False)
  remark = models.CharField(max_length=20)
  timestamp = models.DateTimeField(auto_now_add=True)