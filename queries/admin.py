# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import answer, query
from django.contrib import admin

# Register your models here.
admin.site.register(answer)
admin.site.register(query)