# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from .models import Session 
# Create your views here

def index(request):
    s= Session.objects.all()
    context = {
        'session' : s
            }
    return render(request, 'index.html', context)
