from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # make sure to change the first file name to that which has the views within it,
    # signups in my case
    
    url(r'^$', 'signups.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^userhome/$', 'signups.views.userhome', name='userhome'),
    url(r'^settings/$', 'signups.views.settings', name='settings'),
    url(r'^aboutus/$', 'signups.views.aboutus', name='aboutus'),
    url(r'^thank-you/$', 'signups.views.thankyou', name='thankyou'),
    
    #Handling login, logout, or register   
    url(r'^register/$', 'signups.views.register', name='register'),
    url(r'^login$', 'signups.views.login', name='login'),
    url(r'^logout$', 'signups.views.logout', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    #settings page
) #+ static(settings.MEDIA_URL, picture_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    