from django.contrib import admin
from onedayonejoke.models import Joke, Tag

class JokeAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_time')
    date_hierarchy = 'create_time'
admin.site.register(Joke, JokeAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Tag, TagAdmin)
