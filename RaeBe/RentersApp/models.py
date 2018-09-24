# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

for user in User.objects.all():
    Token.objects.get_or_create(user=user)
# Create your models here.
class TblRent(models.Model):
    id_rent = models.IntegerField(db_column='id_Rent', primary_key=True)  # Field name made lowercase.
    id_clients = models.IntegerField(db_column='id_Clients')  # Field name made lowercase.
    id_clientsrenter = models.IntegerField(db_column='id_ClientsRenter')  # Field name made lowercase.
    id_car = models.IntegerField(db_column='Id_Car')  # Field name made lowercase.
    dateofpickup = models.IntegerField(db_column='DateOfPickUp')  # Field name made lowercase.
    returnday = models.IntegerField(db_column='ReturnDay')  # Field name made lowercase.
    discount = models.IntegerField(db_column='Discount')  # Field name made lowercase.
    acceptence = models.IntegerField(db_column='Acceptence')  # Field name made lowercase.
    starttime = models.IntegerField(db_column='StartTime')  # Field name made lowercase.
    endtime = models.IntegerField(db_column='EndTime')  # Field name made lowercase.
    rentedtime = models.IntegerField(db_column='RentedTime')  # Field name made lowercase.
    approvalextension = models.IntegerField(db_column='ApprovalExtension')  # Field name made lowercase.
    extendedtime = models.IntegerField(db_column='ExtendedTime')  # Field name made lowercase.
    id_penalty = models.IntegerField()
    isover = models.IntegerField(db_column='isOver')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_rent'
