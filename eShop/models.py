from django.db import models

from django.contrib.auth.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to='categoty_images', default='categoty_images/dafault.jpg')
    # description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    old_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    image = models.ImageField(upload_to='products_images')
    hit = models.BooleanField(default=False)
    sale = models.BooleanField(default=False)
    new = models.BooleanField(default=False)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'
    

class BasketQuerySet(models.QuerySet):
    def total_sum(self): 
        return sum([basket.sum() for basket in self])
    
    def total_quantity(self):
        return sum([basket.quantity for basket in self])
    
    
class FavouriteQuerySet(models.QuerySet):
    def total_sum(self):
        return sum([favorite.sum() for favorite in self])
    
    
class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    
    objects = BasketQuerySet.as_manager()
    
    def __str__(self):
        return f'Корзина для {self.user.email} | Продукт: {self.product.name}'
    
    def sum(self):
        return self.product.price * self.quantity
    
    # def total_sum(self):
    #     baskets = Basket.objects.filter(user=self.user) 
    #     return sum([basket.sum() for basket in baskets]) #функция sum которая используется не в цикле for, является встроенной в питон функцией
    
    # def total_quantity(self):
    #     baskets = Basket.objects.filter(user=self.user)
    #     return sum([basket.quantity for basket in baskets])
    
    
class Favourite(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    
    objects = FavouriteQuerySet.as_manager()
    
    def __str__(self):
        return f'Корзина для {self.user.email} | Продукт: {self.product.name}'
    
    def sum(self):
        return self.product.price * self.quantity
    

class Reviews(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self): 
        return f'Отзыв от пользователя {self.user.username} о товаре {self.product.name}' 