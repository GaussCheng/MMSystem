# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Customer'
        db.create_table('customer_management_customer', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10, primary_key=True)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('addr', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('contact', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('tel', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('customer_management', ['Customer'])


    def backwards(self, orm):
        # Deleting model 'Customer'
        db.delete_table('customer_management_customer')


    models = {
        'customer_management.customer': {
            'Meta': {'object_name': 'Customer'},
            'addr': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '13'})
        }
    }

    complete_apps = ['customer_management']