# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from accounts.models import student, society
from django.db import models

# Create your models here.
class resource(models.Model):
    RID = models.IntegerField(primary_key=True)
    CR_SID = models.ForeignKey(student, on_delete=models.CASCADE)
    Year = models.IntegerField()
    Category = models.CharField(max_length=30)
    Branch = models.CharField(max_length=50)
    Location = models.FileField()
    CID = models.ForeignKey(society, on_delete=models.CASCADE)
