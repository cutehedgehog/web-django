from django.contrib import admin
from .models import Provider, Product, ProductCategory, FAQ, Coupon, News, Vacancy, Review

class ProviderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number']

admin.site.register(Provider, ProviderAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'vendor_code', 'image']
    list_editable = ['price']
    
admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(ProductCategory, CategoryAdmin)

class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'date']

admin.site.register(FAQ, FAQAdmin)

class CouponAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'start_date', 'end_date']

admin.site.register(Coupon, CouponAdmin)

class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

admin.site.register(Vacancy, VacancyAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'news_text', 'summary', 'date', 'image']

admin.site.register(News, NewsAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['review_text', 'review_date', 'rate_field']

admin.site.register(Review, ReviewAdmin)