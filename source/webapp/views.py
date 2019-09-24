from django.shortcuts import render, redirect
from .models import Product, cat_choices
from .forms import SearchForm


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
