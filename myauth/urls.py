from django.conf.urls import patterns, include, url
urlpatterns = patterns('myauth.views',
    (r"register/$", 'register_view'),
    (r"login/$", 'login_view'),
    (r"logout/$", 'logout_view'),
    (r"test_post/$", 'test_post'),
)