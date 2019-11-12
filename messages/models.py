# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from accounts.models import student
from django.db import models

# Create your models here.
class message(models.Model):
    MID = models.IntegerField(primary_key=True)
    Sender_ID = models.ForeignKey(student, on_delete=models.CASCADE, related_name='s')
    Reciever_ID = models.ForeignKey(student, on_delete=models.CASCADE, related_name='r')
    Content = models.TextField()
    Timestamp = models.DateTimeField()

    def __str__(self):
        return self.Content