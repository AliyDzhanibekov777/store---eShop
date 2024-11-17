from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('catalog/', views.catalog, name='catalog'),
    path('contacts/', views.contacts, name='contacts'),
    path('delivery/', views.delivery, name='delivery'),
    path('search/', views.search, name='search'),
    path('baskets/checkout', views.checkout, name='checkout'),
    path('reviews/add/<int:product_id>', views.reviews_add, name='reviews_add'),
    path('category/<int:category_id>', views.category, name='category'),
    path('baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),
    path('favourites/add/<int:product_id>/', views.favourite_add, name='favourite_add'),
    path('favourites/remove/<int:favourite_id>/', views.favourite_remove, name='favourite_remove'),
    path('favourites/add_in_basket/<int:product_id>/', views.from_favourite_in_basket_add, name='fav_in_bas')
]