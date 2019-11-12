# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class group(models.Model):
    GID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    Established = models.DateTimeField()
    Current_Member_Count = models.IntegerField()
    Is_Club = models.BooleanField(default=True)
    def __str__(self):
        return self.Name



class student(models.Model):
    SID = models.IntegerField(primary_key=True)
    Name = models.TextField(max_length=50)
    Picture = models.ImageField(upload_to='dp/')
    DOB = models.DateField()
    Email = models.EmailField(blank = True, null = True)
    Contact = models.BigIntegerField(blank = True,null=True)
    Password = models.CharField(max_length=12)
    Last_Login = models.DateTimeField(blank = True, null = True)
    Is_CR = models.BooleanField(default = False)

    def __str__(self):
        return self.Name

class group_members(models.Model):
    SID = models.ForeignKey(student, on_delete=models.CASCADE)
    GID = models.ForeignKey(group, on_delete=models.CASCADE)
    Is_EB = models.BooleanField(default=False)
    Member_Since = models.DateField()

    def __str__(self):
        return self.SID.Name+self.GID.Name

class problems():
    PID = models.IntegerField(primary_key=True)
    Description = models.TextField()
    Category = models.CharField(max_length=50, null = True)
    Reporter_ID = models.ForeignKey(student, on_delete=models.CASCADE)
    Reporting_Time = models.DateTimeField()
    Solution = models.TextField(null=True)