from django.conf.urls import patterns, url

urlpatterns = patterns('customer_management.views',
    url(r'^customer/print_using_lht/(?P<customer_code>\w+)$', 'print_customer_use_lht'),
    url(r'^customer/print_using_sf/(?P<customer_code>\w+)$', 'print_customer_use_sf'),
    url(r'^customer/print_using_suer/(?P<customer_code>\w+)$', 'print_customer_use_suer'),
)
