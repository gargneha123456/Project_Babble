# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from accounts.models import student
from django.db import models

# Create your models here.
class subject(models.Model):
    SID = models.AutoField(primary_key=True)
    Picture = models.ImageField(upload_to='subjects')
    Subject_Code = models.CharField(max_length=6)
    Name = models.TextField()

    def __str__(self):
        return self.Name

class resource(models.Model):
    RID = models.AutoField(primary_key=True)
    Category = models.CharField(max_length=50, choices=(("Assignment","Assignment"), ("Book","Book PDF"),("PPT","Powerpoint Presentation"),("Question Papers","Question Papers")))
    File = models.FileField(upload_to='files/')
    Subject = models.ForeignKey(subject, on_delete=models.CASCADE)
    Details = models.TextField(default='File')
    Timestamp = models.DateTimeField(null = True)
    Uploader= models.ForeignKey(student, on_delete=models.CASCADE, null = True)
    Available = models.BooleanField(default=True)

    def __str__(self):
        return self.Subject


