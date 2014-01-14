# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Photo'
        db.create_table(u'onedayonejoke_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='onedayonejoke/images/default.jpg', max_length=100)),
        ))
        db.send_create_signal(u'onedayonejoke', ['Photo'])

        # Deleting field 'Joke.img'
        db.delete_column(u'onedayonejoke_joke', 'img')

        # Adding field 'Joke.image'
        db.add_column(u'onedayonejoke_joke', 'image',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onedayonejoke.Photo'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Photo'
        db.delete_table(u'onedayonejoke_photo')

        # Adding field 'Joke.img'
        db.add_column(u'onedayonejoke_joke', 'img',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100),
                      keep_default=False)

        # Deleting field 'Joke.image'
        db.delete_column(u'onedayonejoke_joke', 'image_id')


    models = {
        u'onedayonejoke.joke': {
            'Meta': {'ordering': "['create_time']", 'object_name': 'Joke'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'create_time': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 1, 12, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['onedayonejoke.Photo']", 'null': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['onedayonejoke.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'onedayonejoke.photo': {
            'Meta': {'object_name': 'Photo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'onedayonejoke/images/default.jpg'", 'max_length': '100'})
        },
        u'onedayonejoke.tag': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['onedayonejoke']