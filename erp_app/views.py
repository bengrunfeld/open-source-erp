from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import datetime
import time
from django import forms
from erp_app.models import Customers
from django.template import RequestContext, loader

def index(request):
    customer_info = Customers.objects.all()
    context = RequestContext(request, {'customer_info': customer_info,})
    return render(request, 'erp_app/index.html', context)
