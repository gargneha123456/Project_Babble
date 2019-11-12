# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import student, group, group_members

from django.contrib import admin

# Register your models here
admin.site.register(student)
admin.site.register(group)
admin.site.register(group_members)