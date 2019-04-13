# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from accounts.models import student,society
from django.db import models

# Create your models here.
class poll(models.Model):
    PID = models.IntegerField(primary_key=True)
    CR_ID = models.ForeignKey(student, on_delete=models.CASCADE)
    CID = models.ForeignKey(society, on_delete=models.CASCADE)
    Question_File = models.FileField()
    Result_File = models.FileField()