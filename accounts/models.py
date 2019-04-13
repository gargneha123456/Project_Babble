# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class student(models.Model):
    SID = models.IntegerField(primary_key=True)
    Name = models.TextField(max_length=50)
    DOB = models.DateField()
    Branch = models.CharField(max_length=50)
    Email = models.EmailField(null = True)
    Contact = models.BigIntegerField( null=True)
    Password = models.CharField(max_length=12)
    Last_Login = models.DateTimeField()
    Role = models.CharField( max_length=20)

class society(models.Model):
    CID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    Established = models.DateTimeField()
    Current_Member_Count = models.IntegerField()

class society_members(models.Model):
    SID = models.ForeignKey(student, on_delete=models.CASCADE)
    CID = models.ForeignKey(society, on_delete=models.CASCADE)
    Role = models.CharField(max_length=30)
    Member_Since = models.DateField()

class problems():
    PID = models.IntegerField(primary_key=True)
    Description = models.TextField()
    Category = models.CharField(max_length=50, null = True)
    Reporter_ID = models.ForeignKey(student, on_delete=models.CASCADE)
    Reporting_Time = models.DateTimeField()
    Solution = models.TextField(null=True)