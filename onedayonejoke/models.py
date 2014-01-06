from django.db import models
import datetime
import json
from django.core.serializers.json import DjangoJSONEncoder

class Tag(models.Model):
    name=models.CharField(max_length=100,unique=True)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ('name',)

class Joke(models.Model):
    category = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    img = models.ImageField(upload_to='onedayonejoke/images')
    weight = models.IntegerField(default=0)
    create_time = models.DateField(default=datetime.date.today())

    class Meta:
        ordering = ['create_time']

    def add_tags(self, names):
        for name in names:
            try:
                tag = Tag.objects.get(name=name)
            except Tag.DoesNotExist:
                tag = None
            if not tag:
                tag = Tag(name=name) # error code : tag = Tag(name)
                tag.save()
            self.tags.add(tag)

    def to_json(self):
        tags = []
        for tag in self.tags.all():
            tags.append(tag.name)
        return {'id': self.id,'category':self.category, 'tags':tags, 'title': self.title, 'content': self.content,'image':self.img.url, 'weight': self.weight, "create_time": str(self.create_time)}
