from django.conf.urls import patterns, url

from erp_app import views

urlpatterns = patterns('', 
        url(r'^$', views.index, name='index'),
# for future use
#        url(r'^customers/$', views.customers, name='customers'),
#        url(r'^products/^$', views.products, name='products'),
#       url(r'^orders/^$', views.orders, name='orders'),
#        url(r'^invoices/^$', views.invoices, name='invoices'),
#        url(r'^settings/^$', views.settings, name='settings'),
)
