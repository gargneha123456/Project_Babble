# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from accounts.models import student,group
from django.db import models

# Create your models here.
class poll(models.Model):
    PID = models.IntegerField(primary_key=True)
    CR_ID = models.ForeignKey(student, on_delete=models.CASCADE, blank=True, null=True)
    GID = models.ForeignKey(group, on_delete=models.CASCADE, blank=True, null = True)
    Question_File = models.FileField()
    Result_File = models.FileField()
    Subject = models.TextField(null=True)

    def __str__(self):
        return self.Subject