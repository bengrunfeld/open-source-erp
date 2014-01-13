from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
import datetime
import time
from django import forms
from erp_app.models import Expenses
from django.template import RequestContext, loader

from erp_app.models import Orders

def home(request):
	"""View for the Homepage including list of Orders and Expenses""" 
	template = 'erp_app/home.html'
        expenses_info = Expenses.objects.all()
        context = RequestContext(request, {'expenses_info': expenses_info})
	return render(request, template, context)

def customers(request):
	pass

def orders(request):
	pass	

def invoices(request):
	pass	

def products(request):
	pass	

def suppliers(request):
	pass	

def employees(request):
	pass	

def expenses(request):
	pass	

def reports(request):
	pass	

def taxes(request):
	pass	
