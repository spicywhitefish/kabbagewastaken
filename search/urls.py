from django.conf.urls import patterns, url

urlpatterns = patterns('search',
    url(r'^$', 'views.search', name='search'),

)
