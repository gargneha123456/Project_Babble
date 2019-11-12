# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from accounts.models import student
from django.db import models


# Create your models here.
class query(models.Model):
    Query_ID    = models.AutoField(primary_key=True)
    Asker       = models.ForeignKey(student,on_delete=models.CASCADE)
    Content     = models.TextField()
    Timestamp   = models.DateTimeField(null=True, blank=True)
    Subject     = models.TextField(default='Academic')

    def __str__(self):
        return self.Subject

class answer(models.Model):
    Answer_ID = models.IntegerField(primary_key=True)
    QID = models.ForeignKey(query,on_delete=models.CASCADE)
    Respondent = models.ForeignKey(student,on_delete=models.CASCADE)
    Answer = models.TextField()
    Timestamp = models.DateTimeField()

    def __str__(self):
        return self.Answer