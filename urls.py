from django.conf.urls.defaults import patterns, url, include
from main import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wdys.views.home', name='home'),
    # url(r'^wdys/', include('wdys.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.main),
    url(r'^make/$', views.make),
    url(r'^comment/$', views.comment),
    url(r'^upload/$', views.upload),
    url(r'^uploadImages/$', views.uploadImages),
    url(r'^step2/$', views.step2),
    url(r'^step3/$', views.step3),
    url(r'^publish/$', views.publish),
)
