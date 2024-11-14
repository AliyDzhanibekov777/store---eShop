from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from eShop.models import Basket, Favourite


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UserLoginForm()
        
    context = {
        'title': 'Форма входа',
        'form': form,
    }
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegistrationForm()
            
    context = {
        'title': 'Форма регистрации',
        'form': form
    }
    
    return render(request, 'users/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'title': 'Профиль',
        'form': form
    }
    
    return render(request, 'users/profile.html', context)


@login_required
def baskets(request):
    baskets = Basket.objects.filter(user=request.user)
    
    # total_sum = sum([basket.sum() for basket in baskets]) 
    # total_quantity = sum([basket.quantity for basket in baskets])
    
    # total_sum = 0
    # total_quantity = 0
    # for basket in baskets:
    #     total_sum += basket.sum()
    #     total_quantity += basket.quantity
    
    context = {
        'title': 'Корзина',
        'baskets': baskets,
    }
    
    return render(request, 'eShop/baskets.html', context)


@login_required
def favourites(request):
    favourites = Favourite.objects.filter(user=request.user)
    
    # total_sum = 0
    # for favourite in favourites:
    #     total_sum += favourite.sum()
    
    context = {
        'title': 'Корзина',
        'favourites': favourites,    
    }
    
    return render(request, 'eShop/favourites.html', context)