# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.template import RequestContext,loader
# Create your views here.

from django.http import *
from .models import *
def index(request):
    bookList = BookInfo.objects.all()
    context = {'list':bookList}
    return render(request,'booktest/index.html',context)