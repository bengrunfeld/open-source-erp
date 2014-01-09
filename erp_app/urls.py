from django.conf.urls import patterns, url

from erp_app import views

urlpatterns = patterns('', 
        url(r'^$', views.home, name='home'),
)