__author__ = 'shane'

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

    url(r'^$','myapp.views.index' ),
    url(r'^$','myapp.views.home')

)
#urlpatterns = [ss
    #url(r'^$','myapp.views.home')
    #url(r'^admin/',include(admin.site.urls))
#]