from django.contrib import admin
from eShop.models import ProductCategory, Product, Reviews


admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Reviews)