# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MaintainLog'
        db.create_table('maintain_log_maintainlog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['customer_management.Customer'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product_management.Product'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('manufacture_date', self.gf('django.db.models.fields.DateField')()),
            ('carry_date', self.gf('django.db.models.fields.DateField')()),
            ('bug_find_by_customer', self.gf('django.db.models.fields.TextField')()),
            ('bug_find_by_tester', self.gf('django.db.models.fields.TextField')()),
            ('result', self.gf('django.db.models.fields.TextField')()),
            ('maintain_date', self.gf('django.db.models.fields.DateField')()),
            ('receive_express_number', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('invoice_number', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('express', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['express_management.ExpressDelivery'])),
        ))
        db.send_create_signal('maintain_log', ['MaintainLog'])


    def backwards(self, orm):
        # Deleting model 'MaintainLog'
        db.delete_table('maintain_log_maintainlog')


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
        },
        'express_management.expressdelivery': {
            'Meta': {'object_name': 'ExpressDelivery'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'maintain_log.maintainlog': {
            'Meta': {'object_name': 'MaintainLog'},
            'bug_find_by_customer': ('django.db.models.fields.TextField', [], {}),
            'bug_find_by_tester': ('django.db.models.fields.TextField', [], {}),
            'carry_date': ('django.db.models.fields.DateField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['customer_management.Customer']"}),
            'express': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['express_management.ExpressDelivery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_number': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'maintain_date': ('django.db.models.fields.DateField', [], {}),
            'manufacture_date': ('django.db.models.fields.DateField', [], {}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['product_management.Product']"}),
            'receive_express_number': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'result': ('django.db.models.fields.TextField', [], {})
        },
        'product_management.bugtype': {
            'Meta': {'object_name': 'BugType'},
            'decription': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'product_management.product': {
            'Meta': {'unique_together': "(('model', 'version'),)", 'object_name': 'Product'},
            'bug_types': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['product_management.BugType']", 'symmetrical': 'False'}),
            'display': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'release_time': ('django.db.models.fields.DateField', [], {}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['maintain_log']