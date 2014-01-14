# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table(u'onedayonejoke_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'onedayonejoke', ['Tag'])

        # Adding model 'Joke'
        db.create_table(u'onedayonejoke_joke', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('create_time', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 1, 5, 0, 0))),
        ))
        db.send_create_signal(u'onedayonejoke', ['Joke'])

        # Adding M2M table for field tags on 'Joke'
        m2m_table_name = db.shorten_name(u'onedayonejoke_joke_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('joke', models.ForeignKey(orm[u'onedayonejoke.joke'], null=False)),
            ('tag', models.ForeignKey(orm[u'onedayonejoke.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['joke_id', 'tag_id'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table(u'onedayonejoke_tag')

        # Deleting model 'Joke'
        db.delete_table(u'onedayonejoke_joke')

        # Removing M2M table for field tags on 'Joke'
        db.delete_table(db.shorten_name(u'onedayonejoke_joke_tags'))


    models = {
        u'onedayonejoke.joke': {
            'Meta': {'ordering': "['create_time']", 'object_name': 'Joke'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'create_time': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 1, 5, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['onedayonejoke.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'onedayonejoke.tag': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['onedayonejoke']