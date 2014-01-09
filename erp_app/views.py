from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
import datetime
import time
from django import forms

def index(request):
    """View for the Homepage"""    
    template = 'erp_app/home.html'
    return render(request, template)
