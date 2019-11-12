# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from accounts.models import student, group
from django.db import models

# Create your models here.
class Announcement( models.Model ):
    AID = models.AutoField(primary_key=True)
    CR = models.ForeignKey(student,on_delete=models.CASCADE,null = True, blank=True)
    GID = models.ForeignKey(group, on_delete= models.CASCADE, null = True, blank=True)
    Subject = models.TextField(null=True,blank=True)
    Timestamp = models.DateTimeField()
    Content = models.TextField(null=True,blank = True)

    def __str__(self):
        return self.Subject