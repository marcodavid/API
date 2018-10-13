from __future__ import unicode_literals

from django.db import models

class TblClients(models.Model):
    id_clients = models.AutoField(db_column='id_Clients', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100)  # Field name made lowercase.
    isrenter = models.IntegerField(db_column='isRenter')  # Field name made lowercase.
    age = models.DateField(db_column='Age')  # Field name made lowercase.
    curp = models.CharField(db_column='CURP', max_length=18, blank=True, null=True)  # Field name made lowercase.
    telcountry = models.CharField(db_column='TelCountry', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lada = models.IntegerField(db_column='Lada', blank=True, null=True)  # Field name made lowercase.
    telnumber = models.IntegerField(db_column='TelNumber', blank=True, null=True)  # Field name made lowercase.
    id_address = models.IntegerField(db_column='id_Address')  # Field name made lowercase.
    imgprofilephoto = models.CharField(db_column='imgProfilePhoto', max_length=80, blank=True, null=True)  # Field name made lowercase.
    fulldata = models.IntegerField(db_column='fullData')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_clients'






class TblAddress(models.Model):
    id_clients = models.IntegerField(db_column='id_Clients')  # Field name made lowercase.
    id_address = models.AutoField(db_column='id_Address', primary_key=True)  # Field name made lowercase.
    zipcode = models.IntegerField(db_column='ZipCode', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50, blank=True, null=True)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=50, blank=True, null=True)  # Field name made lowercase.
    numint = models.IntegerField(db_column='NumInt', blank=True, null=True)  # Field name made lowercase.
    numext = models.IntegerField(db_column='NumExt', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_address'

class TblDriverlicense(models.Model):
    id_clients = models.IntegerField(db_column='id_Clients')  # Field name made lowercase.
    id_driverlicense = models.AutoField(db_column='id_DriverLicense', primary_key=True)  # Field name made lowercase.
    licensenum = models.CharField(db_column='LicenseNum', max_length=10, blank=True, null=True)  # Field name made lowercase.
    startday = models.DateField(db_column='StartDay', blank=True, null=True)  # Field name made lowercase.
    endday = models.DateField(db_column='EndDay', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_driverlicense'

