from django.db import models
from django.urls import reverse
from login.models import MyUser
        
class Provider(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    worker = models.ForeignKey(MyUser, related_name='providers', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"
       
    def sort_products(self):
        return reverse('shop:list_products_by_provider', args=[self.name])

    def get_absolute_url(self):
        return reverse('shop:provider_details', args=[str(self.name)])

class ProductCategory(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vendor_code = models.CharField(max_length=20)
    provider = models.ForeignKey(
        Provider, related_name='products', on_delete=models.CASCADE)
    categories = models.ManyToManyField(ProductCategory)
    image = models.ImageField(upload_to='user/', default='user/test.jpg')

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_details', args=[str(self.id)])


class FAQ(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField(blank=False)
    date = models.DateField()


class Review(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING)
    review_text = models.TextField(blank=True)
    review_date = models.DateField()
    rate_field = models.IntegerField(default=5)


class News(models.Model):
    title = models.CharField(max_length=100)
    news_text = models.TextField(blank=False)
    summary = models.TextField(blank=False, default="news text")
    date = models.DateField()
    image = models.ImageField(upload_to='user/', default='user/test.jpg')


class Vacancy(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()


class Coupon(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

