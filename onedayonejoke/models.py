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

class Photo(models.Model):
    image = models.ImageField(upload_to='onedayonejoke/images', default = 'onedayonejoke/images/default.jpg')

    def to_json(self):
        return {'id': self.id, 'url': self.image.url}

class Joke(models.Model):
    category = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ForeignKey(Photo, null=True)
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
        if self.image:
            image_url = self.image.image.url
        else:
            image_url = ""
        return {'id': self.id,'category':self.category, 'tags':tags, 'title': self.title, 'content': self.content,'image_url': image_url, 'weight': self.weight, "create_time": str(self.create_time)}
