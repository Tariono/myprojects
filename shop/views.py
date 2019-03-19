from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Product
from .utils import *
from .forms import ProductForm

# Create your views here.

def products_list(request):
    search_query = request.GET.get('search')
    if search_query:
        products = Product.objects.filter(Q(title__icontains=search_query)| Q(body__icontains=search_query))
    else:
        products = Product.objects.all()


    paginator = Paginator(products,15)
    page_number = request.GET.get('page',1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''

    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''


    context= {'page_object': page,
        'is_paginated':is_paginated,
        'next_url':next_url,
        'prev_url':prev_url}
    return render(request, 'shop/products_list.html', context=context)


#def ProductDetail(request, id, slug):
    #product = get_object_or_404(Product, id=id, slug=slug, available=True)
    #cart_product_form = CartAddProductForm()
    #return render_to_response('shop/product/detail.html',
    #                         {'product': product,
    #                          'cart_product_form': cart_product_form})

class ProductDetail(ObjectDetailMixin, View):
    model = Product
    template = 'shop/product_detail.html'

class ProductCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = ProductForm
    template = 'shop/product_create_form.html'
    raise_exception=True

class ProductUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Product
    form_model = ProductForm
    template = 'shop/product_update_form.html'
    raise_exception=True

class ProductDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Product
    template = 'shop/product_delete_form.html'
    redirect_url = 'product_list_url'
    raise_exception=True
