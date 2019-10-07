from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.contrib.auth.decorators import login_required

def product_list(request, category_slug=None):
 
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(active_item=True)
    
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'check' : 2,
    }
    return render(request, 'shop/product/list.html', context)
    
    return render(request, 'shop/product/list.html', {'check':1})

@login_required(login_url='/login')
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, active_item=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
        'check' : 2,
    }
    return render(request, 'shop/product/detail.html', context)

