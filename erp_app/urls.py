from django.conf.urls import patterns, url

from erp_app import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='home'),
	url(r'^customers/$', views.customers, name='customers'),
	url(r'^orders/$', views.orders, name='orders'),
	url(r'^invoices/$', views.invoices, name='invoices'),
	url(r'^products/$', views.products, name='products'),
	url(r'^suppliers/$', views.settings, name='suppliers'),
	url(r'^employees/$', views.settings, name='employees'),
	url(r'^expenses/$', views.settings, name='expenses'),
	url(r'^reports/$', views.settings, name='reports'),
	url(r'^taxes/$', views.settings, name='taxes'),
	url(r'^settings/$', views.settings, name='settings'),
)
