from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
import datetime
import time
from django import forms
from erp_app.models import Expenses
from django.template import RequestContext, loader

from erp_app.models import Orders

def index(request):
	"""View for the Homepage including list of Orders and Expenses""" 
	template = 'erp_app/home.html'
        expenses_info = Expenses.objects.all()
        context = RequestContext(request, {'expenses_info': expenses_info})
	return render(request, template, context)
