from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

# Create your views here.

# Creating products
def create_product(request):
    if request.method == "POST":
        new_product_form = ProductForm(request.POST)
        if new_product_form.is_valid():
            new_product_form.save()
            return redirect('product_list')
    else:
        new_product_form = ProductForm() 
    return render(request, "products/product_form.html", {"form": new_product_form})

# Getting all products
def get_products(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products": products})

# Updating the product
def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)  
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)  
    return render(request, "products/product_form.html", {"form": form})  

# Deleting the product
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)  
    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    return render(request, "products/product_confirm.html", {"product": product})
#defining home view
def home_view(request):
    return render(request,"products/home.html")