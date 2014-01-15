from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
import datetime
import time
from django import forms
from erp_app.models import Expenses
from django.template import RequestContext, loader

from erp_app.models import * 

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

def settings(request):
	pass	

def filldb(request):
    """Automatically fills the database with Dummy Data""" 

    # Sets the time
    t = datetime.datetime.now()    

    # Record set 1                                                                  
    e = Expenses(expense_name='Rent', description='Our monthly rent',           
        date_paid=t, amount_paid=500)                                           
    e.save()                                                                    
                                                                                
    p = Products(name='Orange', description='A round fruity ball', price=5)     
    p.save()                                                                    
    product = Products.objects.get(pk=1)                                        
                                                                                
    c = Customers(title='Mr', first_name='OJ', middle_name="Jeremy",            
        last_name="Simpson", suffix="Jr", email="orange@juice.com",             
        company="Slashers Inc", display_name="OJ",                              
        print_on_check_as="OJ Simpson", billing_street="320 Madison Ave",       
        billing_city="San Francisco", billing_state="CA", billing_zip="30284",  
        billing_country="USA", shipping_street="320 Madison Ave",               
        shipping_city="San Francisco", shipping_state="CA",                     
        shipping_zip="30284", shipping_country="USA",                           
        other_details="cant be trusted")                                        
    c.save()                                                                    
    cust = Customers.objects.get(pk=1)                                          
                                                                                
    o = Orders(cust_id=cust, invoice_creation_date=t, delivery_due_date=t,      
        payment_due_date=t, custom_message="Place in the back entrance")        
    o.save()                                                                    
    order = Orders.objects.get(pk=1)                                            
                                                                                
    op = Orders_Products(order_id=order, product_id=product, quantity=50)       
    op.save()

    # Record set 2                                                                   
    e = Expenses(expense_name='Electricity',                                    
        description='Our monthly Electricity', date_paid=t,                     
        amount_paid=350.75)
    e.save()

    p = Products(name='Apple', description='Keeps the doctor away', price=4)    
    p.save()
    product = Products.objects.get(pk=2)

    c = Customers(title='Miss', first_name='Heather', middle_name="Peri",       
        last_name="Middleton", suffix="", email="middleton@castle.com",         
        company="Winstons", display_name="Middleton",                           
        print_on_check_as="Winstons", billing_street="520 Terracotta Ave",      
        billing_city="England", billing_state="UK", billing_zip="73329",        
        billing_country="UK", shipping_street="520 Terracotta Ave",             
        shipping_city="England", shipping_state="UK", shipping_zip="73329",     
        shipping_country="UK", other_details="possibly royalty")                
    c.save()
    cust = Customers.objects.get(pk=2)

    o = Orders(cust_id=cust, invoice_creation_date=t, delivery_due_date=t,       
        payment_due_date=t, custom_message="Give the cheese to Sam")            
    o.save()
    order = Orders.objects.get(pk=2)

    op = Orders_Products(order_id=order, product_id=product, quantity="35") 
    op.save()


    # Record set 3
    e = Expenses(expense_name='Gas',                                            
        description='Our monthly Gas', date_paid=t,                             
        amount_paid=275.15)
    e.save()

    p = Products(name='Apple', description='Keeps the doctor away', price=4)
    p.save()
    product = Products.objects.get(pk=3)

    c = Customers(title='Miss', first_name='Heather', middle_name="Peri",       
        last_name="Middleton", suffix="", email="middleton@castle.com",         
        company="Winstons", display_name="Middleton",                           
        print_on_check_as="Winstons", billing_street="520 Terracotta Ave",      
        billing_city="England", billing_state="UK", billing_zip="73329",        
        billing_country="UK", shipping_street="520 Terracotta Ave",             
        shipping_city="England", shipping_state="UK", shipping_zip="73329",     
        shipping_country="UK", other_details="possibly royalty")
    c.save()
    cust = Customers.objects.get(pk=3)

    o = Orders(cust_id=cust, invoice_creation_date=t, delivery_due_date=t,       
        payment_due_date=t, custom_message="Give the cheese to Sam")
    o.save()
    order = Orders.objects.get(pk=3)

    op = Orders_Products(order_id=order, product_id=product, quantity="35")
    op.save()
                                                                     
    # Record set 4                                                                            
    e = Expenses(expense_name='Land Tax', description='Our monthly Land Tax',   
        date_paid=t, amount_paid=146.23)
    e.save()

    p = Products(name='Rubix Cube', description='A puzzling square', price=20)
    p.save()
    product = Products.objects.get(pk=4)

    c = Customers(title='Mr', first_name='John', middle_name="",                
        last_name="Prescott", suffix="", email="john@prescott.com",             
        company="Prescott's", display_name="Prescott's",                        
        print_on_check_as="Prescott's", billing_street="12 Richy Lane",         
        billing_city="Hoboken", billing_state="NY", billing_zip="54109",        
        billing_country="USA", shipping_street="12 Richy Lane",                 
        shipping_city="Hoboken", shipping_state="NY", shipping_zip="54109",     
        shipping_country="USA", other_details="Extremely loyal to our brand. Don't know why")
    c.save()
    cust = Customers.objects.get(pk=4)

    o = Orders(cust_id=cust, invoice_creation_date=t, delivery_due_date=t,       
        payment_due_date=t, custom_message="Send Rubix Cubes to everyone")
    o.save()
    order = Orders.objects.get(pk=4)
    
    op = Orders_Products(order_id=order, product_id=product, quantity="12")
    op.save()

    template = 'erp_app/filldb.html'
    return render(request, template)


def wipedb(request):
    Customers.objects.all().delete()
    Products.objects.all().delete()
    Orders.objects.all().delete()
    Orders_Products.objects.all().delete()
    General_Settings.objects.all().delete()
    Expenses.objects.all().delete()

    template = 'erp_app/wipedb.html'                                            
    return render(request, template)
