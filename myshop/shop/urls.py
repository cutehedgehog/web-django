from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('about_company/', views.about_company, name='about'),
    path('faq/', views.faq, name='faq'),
    path('tags_page/', views.tags_page, name='tags_page'),
    path('news/', views.news, name='news'),
    path('news/<int:id>', views.news_article, name='news_article'),
    path('reviews/', views.reviews, name='reviews'),
    path('create_review/', views.create_review, name='create_review'),
    path('coupons/', views.coupons, name='coupons'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('contacts/', views.contacts, name='contacts'),
    path('create_product/<str:provider_name>', views.create_product, name='create_product'),
    path('list_products/', views.product_list, name='list_products'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('list_products/<int:id>', views.product_details, name='product_details'),
    path('delete_product/<int:id>', views.delete_product, name='delete_product'),
    path('edit_product/<str:provider_name>/<int:id>/', views.edit_product, name='edit_product'),
    path('list_products/<str:name>', views.provider_details, name='provider_details'),
    path('list_products/<str:product_provider_name>/', views.product_list,
         name='list_products_by_provider'
         ),
]
