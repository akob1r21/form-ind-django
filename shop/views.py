from django.shortcuts import render, HttpResponse, redirect
from .models import Product, Category
from django.contrib.auth.decorators import (
    login_required, permission_required, user_passes_test)
from .forms import CategoryForm, ProductForm



def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Category.objects.create(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
            )
            print('salom==============')
            return redirect('products')
        
    else:
        form = CategoryForm()
        return render(request, 'products/form.html',
                      {'title':'Create Category','form':form})















@login_required
@permission_required('shop.view_product', raise_exception=True)
def product_list(request):
    products = Product.objects.select_related('category')

    return render(request, 'products/list.html', {'products':products})



@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()
        return render(request, 'products/form.html',
                      {'title':'Create Product','form':form})

def is_seller(user):
    return user.groups.filter(name='Sellers').exists()

# @user_passes_test(is_seller, login_url='login')
def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm(instance=product)
        return render(request, 'products/form.html',
                      {'title':'Create Product','form':form})    





