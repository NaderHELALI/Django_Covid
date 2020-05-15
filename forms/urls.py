# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 15:18:25 2020

@author: sohan
"""

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),

]
