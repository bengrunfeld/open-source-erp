from django.conf.urls import patterns, url

from erp_app import views

urlpatterns = patterns('', 
	url(r'^$', views.home, name='home'),
	url(r'^customers/$', views.customers, name='customers'),
	url(r'^orders/$', views.orders, name='orders'),
	url(r'^invoices/$', views.invoices, name='invoices'),
	url(r'^products/$', views.products, name='products'),
	url(r'^suppliers/$', views.suppliers, name='suppliers'),
	url(r'^employees/$', views.employees, name='employees'),
	url(r'^expenses/$', views.expenses, name='expenses'),
	url(r'^reports/$', views.reports, name='reports'),
	url(r'^taxes/$', views.taxes, name='taxes'),
	url(r'^settings/$', views.settings, name='settings'),
)
