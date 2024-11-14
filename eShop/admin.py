from django.contrib import admin
from eShop.models import ProductCategory, Product


admin.site.register(Product)
admin.site.register(ProductCategory)