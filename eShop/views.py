from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from django.contrib import messages
from django.urls import reverse

from eShop.models import ProductCategory, Product, Basket, Favourite, Reviews

from .forms import ReviewForm


def home(request):
    context = {
        'title': 'Главная',        
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    
    return render(request, 'eShop/home.html', context)


def about(request):
    context = {
        'title': 'О нас'
    }
    
    return render(request, 'eShop/about.html', context)


def category(request, category_id):
    category = ProductCategory.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    
    context = {
        'title': 'Каталог',
        'categories': ProductCategory.objects.all(),
        'products': products
    }
    
    return render(request, 'eShop/category.html', context)


def catalog(request):
    context = {
        'title': 'Каталог',
        'categories': ProductCategory.objects.all()
    }
    
    return render(request, 'eShop/catalog.html', context)


def contacts(request):
    context = {
        'title': 'Контракты'
    }
    
    return render(request, 'eShop/contacts.html', context)


def delivery(request):
    context = {
        'title': 'Доставка'
    }
    
    return render(request, 'eShop/delivery.html', context)
    
    
@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def favourite_add(request, product_id):
    product = Product.objects.get(id=product_id)
    favourites = Favourite.objects.filter(user=request.user, product=product)
    
    if not favourites.exists():
        Favourite.objects.create(user=request.user, product=product, quantity=1)
    else:
        favourite = favourites.first()
        favourite.quantity += 1
        favourite.save()
        
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def favourite_remove(request, favourite_id):
    favourites = Favourite.objects.get(id=favourite_id)
    favourites.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def from_favourite_in_basket_add(request, product_id):
    # print(product_id)
    product = get_object_or_404(Product, id=product_id)
    # product = Product.objects.get(id=product_id)
    favourite_item = Favourite.objects.filter(user=request.user, product=product).first()
    basket_item = Basket.objects.filter(user=request.user, product=product).first() 
    if basket_item:
        basket_item.quantity += favourite_item.quantity
        basket_item.save()
    else:
        Basket.objects.create(user=request.user, product=product, quantity=favourite_item.quantity)
    favourite_item.delete()      
        
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def search(request):
    query = request.GET.get('s', '')
    products = Product.objects.filter(name__icontains=query) if query else []
    context = {
        'title': 'Поиск',
        'products': products,
        'query': query
    }
    
    return render(request, 'eShop/search.html', context)
    

def reviews(request, product_id):
    product = Product.objects.get(id=product_id)
    review = Reviews.objects.filter(user=request.user, product=product)
    context = {
        'title': 'Отзывы',
        'products': review
    }

    return render(request, 'eShop/reviews.html', context)


def reviews_add(request):
    if request.method == 'POST':
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Комментарий успешно добавлен!')
            return HttpResponseRedirect(reverse('reviews'))  
    else:
        form = ReviewForm()

    context = {
        'title': 'Отзывы',
        'form': form
    }    

    return render(request, 'eShop/reviews.html', context)


# def reviews_add(request, product_id):
#     product = Product.objects.get(id=product_id)
#     review = Reviews.objects.filter(user=request.user, product=product)

#     if request.method == 'POST':
#         form = ReviewForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Комментарий успешно добавлен!')
#             return HttpResponseRedirect(reverse('reviews'))  
#     else:
#         form = ReviewForm()

#     context = {
#         'title': 'Отзывы',
#         'products': review
#     }    

#     return render(request, 'eShop/reviews.html', context)
