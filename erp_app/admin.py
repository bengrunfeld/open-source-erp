from django.contrib import admin
from erp_app.models import Expenses, Orders, Products, Orders_Products, Customers

class Orders_Products_Inline(admin.TabularInline):
    model = Orders_Products
    extra = 3

class OrdersAdmin(admin.ModelAdmin):
    inlines = [Orders_Products_Inline]

# Register your models here.

admin.site.register(Expenses)
admin.site.register(Customers)
admin.site.register(Products)
admin.site.register(Orders, OrdersAdmin)
