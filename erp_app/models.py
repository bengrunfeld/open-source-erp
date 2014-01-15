from django.db import models

# Create your models here.

class Customers(models.Model):
    title = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200) 
    last_name = models.CharField(max_length=200)
    suffix = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    # display_name = models.CharField(max_length=200)
    # print_on_check_as = models.CharField(max_length=200)
    # billing_street = models.CharField(max_length=200)
    # billing_city = models.CharField(max_length=200)
    # billing_state = models.CharField(max_length=2)
    # billing_zip = models.CharField(max_length=10)
    # billing_country = models.CharField(max_length=200) 
    # shipping_street = models.CharField(max_length=200)
    # shipping_city = models.CharField(max_length=200)
    # shipping_state = models.CharField(max_length=2)
    # shipping_zip = models.CharField(max_length=10)
    # shipping_country = models.CharField(max_length=200)   
    # other_details = models.CharField(max_length=500)
    def __unicode__(self):  
        return self.first_name + " "  + self.last_name 

class Products(models.Model):
    name = models.CharField(max_length=500) 
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __unicode__(self):  
        return self.name

class Orders(models.Model):
    cust_id = models.ForeignKey(Customers)
    invoice_creation_date = models.DateTimeField('Invoice Created Date')
    invoice_number = models.CharField(max_length=100)
    delivery_due_date = models.DateTimeField('Delivery Due Date')
    payment_due_date = models.DateTimeField('Payment Due Date') 
    custom_message = models.TextField()
    purchases = models.ManyToManyField(Products, through='Orders_Products')
  
class Orders_Products(models.Model):
    order_id = models.ForeignKey(Orders)
    product_id = models.ForeignKey(Products)
    quantity = models.IntegerField(default=0)

    def cost(self):
        costs = self.quantity * self.product_id.price
        return costs
           
class General_Settings(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)

class Expenses(models.Model):
    expense_name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    date_paid = models.DateTimeField('Expenses Paid Date')
    amount_paid = models.DecimalField(max_digits=20, decimal_places=2)

    def __unicode__(self):  
        return self.expense_name    
