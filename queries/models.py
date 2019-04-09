# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
    xyx