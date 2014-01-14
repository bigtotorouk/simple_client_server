from django.conf.urls import patterns, include, url
urlpatterns = patterns('onedayonejoke.views',
    (r"^jokes/$", 'jokes'),
    (r"^jokes/(?P<joke_id>\d+)/$", "joke"),
    (r"^jokes/weight/$", 'joke_weight'),
    (r"^upload/$", 'upload_file'),
)

