# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BugType'
        db.create_table('product_management_bugtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('decription', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('product_management', ['BugType'])

        # Adding model 'Product'
        db.create_table('product_management_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('display', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('release_time', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('product_management', ['Product'])

        # Adding unique constraint on 'Product', fields ['model', 'version']
        db.create_unique('product_management_product', ['model', 'version'])

        # Adding M2M table for field bug_types on 'Product'
        db.create_table('product_management_product_bug_types', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm['product_management.product'], null=False)),
            ('bugtype', models.ForeignKey(orm['product_management.bugtype'], null=False))
        ))
        db.create_unique('product_management_product_bug_types', ['product_id', 'bugtype_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Product', fields ['model', 'version']
        db.delete_unique('product_management_product', ['model', 'version'])

        # Deleting model 'BugType'
        db.delete_table('product_management_bugtype')

        # Deleting model 'Product'
        db.delete_table('product_management_product')

        # Removing M2M table for field bug_types on 'Product'
        db.delete_table('product_management_product_bug_types')


    models = {
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

    complete_apps = ['product_management']