from django.shortcuts import render, redirect
from .models import Product, cat_choices
from .forms import SearchForm, ProductForm


def main_page(request):
    if request.method == "GET":
        products = Product.objects.filter(balance__gt=0).order_by('category', 'name')
        return render(request, 'index.html', {'products': products, 'choices': cat_choices, 'form': SearchForm})
    elif request.method == "POST":
        bound_form = SearchForm(request.POST)
        if bound_form.is_valid():
            search_query = bound_form.cleaned_data['search_query']
            products = Product.objects.filter(name__icontains=search_query).filter(balance__gt=0).order_by('category',
                                                                                                           'name')
            return render(request, 'index.html', {'products': products, 'choices': cat_choices, 'form': SearchForm})
        return redirect('main_url')


def details_page(request, pk):
    product = Product.objects.get(pk=pk)
    cat = product.category
    for i in cat_choices:
        if cat in i:
            cat = i[1]
    return render(request, 'details_page.html', {'product': product, 'category': cat})


def product_create(request):
    if request.method == "GET":
        return render(request, 'product_create.html', {'form': ProductForm})
    elif request.method == "POST":
        bound_from = ProductForm(request.POST)
        if bound_from.is_valid():
            bound_from.save()
            return redirect('main_url')
        return render(request, 'product_create.html', context={'form': bound_from})


def product_edit(request, pk):
    if request.method == "GET":
        product = Product.objects.get(pk=pk)
        form = ProductForm(instance=product)
        return render(request, 'product_edit.html', {'form': form, 'pk1': pk, 'name': product.name})
    elif request.method == 'POST':
        obj = Product.objects.get(pk=pk)
        bound_from = ProductForm(request.POST, instance=obj)
        if bound_from.is_valid():
            bound_from.save()
            return redirect('main_url')
        return render(request, 'product_edit.html', context={'form': bound_from})


def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', {'product': product})
    elif request.method == 'POST':
        product.delete()
        return redirect('main_url')


def cat_list(request, slug):
    name_in_rus = ''
    for i in cat_choices:
        if slug in i:
            name_in_rus = i[1]
    if request.method == 'GET':
        products = Product.objects.filter(category=slug).filter(balance__gt=0).order_by('name')
        return render(request, 'index.html',
                      {'products': products, 'sel_cat': name_in_rus, 'choices': cat_choices, 'form': SearchForm,
                       'slug': slug})
    elif request.method == 'POST':
        bound_form = SearchForm(request.POST)
        if bound_form.is_valid():
            search_query = bound_form.cleaned_data['search_query']
            products = Product.objects.filter(name__icontains=search_query).filter(category=slug).filter(
                balance__gt=0).order_by('name')
            return render(request, 'index.html',
                          {'products': products, 'sel_cat': name_in_rus, 'choices': cat_choices, 'form': SearchForm,
                           'slug': slug})
        return redirect('main_url', slug=slug)
