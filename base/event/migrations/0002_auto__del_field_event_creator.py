# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Event.creator'
        db.delete_column(u'event_event', 'creator_id')


    def backwards(self, orm):
        # Adding field 'Event.creator'
        db.add_column(u'event_event', 'creator',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=datetime.datetime(2013, 7, 1, 0, 0), to=orm['auth.User']),
                      keep_default=False)


    models = {
        u'event.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'time': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['event']