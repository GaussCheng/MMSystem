from django.shortcuts import render_to_response
from customer_management.models import Customer


def print_customer_use_lht(request, customer_code):
    customer = Customer.objects.get(code=customer_code)
    return render_to_response('customer_management/print_lht.html',
                              {'customer': customer})
    
def print_customer_use_sf(request, customer_code):
    customer = Customer.objects.get(code=customer_code)
    return render_to_response('customer_management/print_sf.html',
                              {'customer': customer})
    
def print_customer_use_suer(request, customer_code):
    customer = Customer.objects.get(code=customer_code)
    return render_to_response('customer_management/print_suer.html',
                              {'customer': customer})
    
def print_customers(request, queryset, express_template_url):
    customers = queryset
    return render_to_response('customer_management/print_customers.html',
                              {'customers':customers,
                               'template_url':express_template_url})
    
def print_customers_use_lht(request, queryset):
    return print_customers(request, queryset, 'print_using_lht')

def print_customers_use_sf(request, queryset):
    return print_customers(request, queryset, 'print_using_sf')

def print_customers_use_suer(request, queryset):
    return print_customers(request, queryset, 'print_using_suer')

