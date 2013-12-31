from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
import datetime
import time
from django import forms

def index(request):
    """Say Hello"""    
    template = 'erp_app/index.html'
    return render(request, template)