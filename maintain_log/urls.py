from django.conf.urls import patterns, url

urlpatterns = patterns('maintain_log.views',
    url(r'^$', 'print_to_html'),
)
