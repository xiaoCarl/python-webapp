# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Demoapp(models.Model):
    demo_id = models.CharField(max_length=10)
    ceate_time = models.DateTimeField(auto_now=True)
    demo_content = models.CharField(max_length=50)
   # def __str__(self):
   #     return self.name


        
    
