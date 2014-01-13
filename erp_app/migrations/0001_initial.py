# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Customers'
        db.create_table(u'erp_app_customers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('suffix', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'erp_app', ['Customers'])

        # Adding model 'Orders'
        db.create_table(u'erp_app_orders', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cust_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erp_app.Customers'])),
            ('invoice_creation_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('delivery_due_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('payment_due_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('custom_message', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'erp_app', ['Orders'])

        # Adding model 'Products'
        db.create_table(u'erp_app_products', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
        ))
        db.send_create_signal(u'erp_app', ['Products'])

        # Adding model 'Orders_Products'
        db.create_table(u'erp_app_orders_products', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erp_app.Orders'])),
            ('product_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erp_app.Products'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'erp_app', ['Orders_Products'])

        # Adding model 'General_Settings'
        db.create_table(u'erp_app_general_settings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'erp_app', ['General_Settings'])


    def backwards(self, orm):
        # Deleting model 'Customers'
        db.delete_table(u'erp_app_customers')

        # Deleting model 'Orders'
        db.delete_table(u'erp_app_orders')

        # Deleting model 'Products'
        db.delete_table(u'erp_app_products')

        # Deleting model 'Orders_Products'
        db.delete_table(u'erp_app_orders_products')

        # Deleting model 'General_Settings'
        db.delete_table(u'erp_app_general_settings')


    models = {
        u'erp_app.customers': {
            'Meta': {'object_name': 'Customers'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'erp_app.general_settings': {
            'Meta': {'object_name': 'General_Settings'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'erp_app.orders': {
            'Meta': {'object_name': 'Orders'},
            'cust_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp_app.Customers']"}),
            'custom_message': ('django.db.models.fields.TextField', [], {}),
            'delivery_due_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            'payment_due_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'erp_app.orders_products': {
            'Meta': {'object_name': 'Orders_Products'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp_app.Orders']"}),
            'product_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp_app.Products']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'erp_app.products': {
            'Meta': {'object_name': 'Products'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'})
        }
    }

    complete_apps = ['erp_app']