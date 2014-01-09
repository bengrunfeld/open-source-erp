from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
import datetime
import time
from django import forms

from erp_app.models import Orders

def index(request):
	"""View for the Homepage including list of Orders and Expenses""" 
	template = 'erp_app/home.html'
	return render(request, template)
