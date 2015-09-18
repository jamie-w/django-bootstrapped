from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    # external libraries
    url(r'^admin/', include(admin.site.urls)),
    url(r'^jsreverse/$', 'django_js_reverse.views.urls_js', name='js_reverse'),

    # the project
    url(r'^$', TemplateView.as_view(template_name='homepage.html'), name='home'),

)
