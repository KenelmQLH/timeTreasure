# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Projects(models.Model):
    pid = models.BigAutoField(primary_key=True)
    pname = models.CharField(max_length=40)
    ptime = models.DecimalField(max_digits=12, decimal_places=1,default=0)
    pdate = models.DateField(blank=True, null=True, auto_now_add=True)
    users = models.ForeignKey(to="Users", to_field="uid", on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'projects'


class Records(models.Model):
    rid = models.BigAutoField(primary_key=True)
    rtime = models.IntegerField()
    rdate = models.DateField(blank=True, null=True,auto_now_add=True)
    # spid = models.IntegerField()
    subprojects = models.ForeignKey(to="Subprojects", to_field="spid", on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'records'


class Subprojects(models.Model):
    spid = models.BigAutoField(primary_key=True)
    spname = models.CharField(max_length=40)
    sptime = models.DecimalField(max_digits=12, decimal_places=1,default=0)
    spdate = models.DateField(blank=True, null=True,auto_now_add=True)
    numrecord = models.IntegerField(default=0)
    # pid = models.IntegerField()
    projects = models.ForeignKey(to="Projects", to_field="pid", on_delete=models.CASCADE)


    class Meta:
        managed = False
        db_table = 'subprojects'


class Users(models.Model):
    uid = models.BigAutoField(primary_key=True)
    uname = models.CharField(max_length=40)
    password = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'users'
