# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from accounts.models import student
from django.db import models


# Create your models here.
class query(models.Model):
    Query_ID    = models.IntegerField()
    Asker_ID    = models.IntegerField()
    Content     = models.TextField()
    Timestamp   = models.DateTimeField()
    Category    = models.TextField()
    Year        = models.IntegerField()
    Branch      = models.TextField()
    Society_ID  = models.IntegerField()

class answer(models.Model):
    Answer_ID = models.IntegerField(primary_key=True)
    QID = models.ForeignKey(query,on_delete=models.CASCADE)
    Respondent_ID = models.ForeignKey(student,on_delete=models.CASCADE)
    Answer = models.TextField()
    Timestamp = models.DateTimeField()