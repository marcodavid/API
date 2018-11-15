# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

for user in User.objects.all():
    Token.objects.get_or_create(user=user)
# Create your models here.
class TblRent(models.Model):
    id_rent = models.AutoField(db_column='id_Rent', primary_key=True)  # Field name made lowercase.
    id_clients = models.IntegerField(db_column='id_Clients')  # Field name made lowercase.
    clientname = models.CharField (db_column='clientName', max_length=50)  # Field name made lowercase.
    id_clientsrenter = models.IntegerField(db_column='id_ClientsRenter')  # Field name made lowercase.
    id_car = models.CharField (db_column='Id_Car', max_length=50)  # Field name made lowercase.
    dateofpickup = models.DateField(db_column='DateOfPickUp')  # Field name made lowercase.
    returnday = models.DateField(db_column='ReturnDay')  # Field name made lowercase.
    discount = models.IntegerField(db_column='Discount')  # Field name made lowercase.
    acceptence = models.IntegerField(db_column='Acceptence')  # Field name made lowercase.
    starttime = models.IntegerField(db_column='StartTime')  # Field name made lowercase.
    endtime = models.IntegerField(db_column='EndTime')  # Field name made lowercase.
    rentedtime = models.IntegerField(db_column='RentedTime')  # Field name made lowercase.
    approvalextension = models.IntegerField(db_column='ApprovalExtension')  # Field name made lowercase.
    extendedtime = models.IntegerField(db_column='ExtendedTime')  # Field name made lowercase.
    id_penalty = models.IntegerField()
    isover = models.IntegerField(db_column='isOver')  # Field name made lowercase.
    price = models.FloatField(db_column='price')
    iva = models.FloatField(db_column='iva')
    totaldays = models.IntegerField (db_column='totaldays')
    totalprice = models.FloatField(db_column='totalPrice')  # Field name made lowercase.
    gain = models.FloatField(db_column='gain')
    pricexiva = models.FloatField (db_column='priceXiva')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tbl_rent'

        
class TblRentpreferences(models.Model):
    id_clients = models.IntegerField()
    firsthour = models.IntegerField(db_column='firstHour')  # Field name made lowercase.
    lasthour = models.IntegerField(db_column='lastHour')  # Field name made lowercase.
    daysbeforerent = models.IntegerField(db_column='daysBeforeRent')  # Field name made lowercase.
    mintime = models.IntegerField(db_column='minTime')  # Field name made lowercase.
    maxtime = models.IntegerField(db_column='maxTime')  # Field name made lowercase.
    id_rentpreferences = models.AutoField(db_column='id_rentPreferences', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_rentpreferences'

class RelationsComments(models.Model):
    id_messages = models.AutoField(primary_key=True)
    id_clientsreceiver = models.IntegerField(db_column='id_ClientsReceiver')  # Field name made lowercase.
    id_clientscommenter = models.IntegerField(db_column='id_ClientsCommenter')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500)  # Field name made lowercase.
    rate = models.IntegerField(db_column='Rate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relations_comments'
