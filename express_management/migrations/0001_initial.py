# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ExpressDelivery'
        db.create_table('express_management_expressdelivery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tel', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('express_management', ['ExpressDelivery'])


    def backwards(self, orm):
        # Deleting model 'ExpressDelivery'
        db.delete_table('express_management_expressdelivery')


    models = {
        'express_management.expressdelivery': {
            'Meta': {'object_name': 'ExpressDelivery'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['express_management']