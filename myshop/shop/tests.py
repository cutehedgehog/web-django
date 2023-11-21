from django.test import TestCase, Client
from django.urls import reverse
from login.models import MyUser
from .models import Product, Provider, ProductCategory
from contextlib import contextmanager
from datetime import date


class TravelAppTests(TestCase):
    @contextmanager
    def modify_user_is_staff(self, user, is_staff):
        original_is_staff = user.is_staff
        user.is_staff = is_staff
        user.save()
        yield
        user.is_staff = original_is_staff
        user.save()

    def setUp(self):
        self.client = Client()
        self.user = MyUser.objects.create_user(email="test@gmail.com",
            username='testuser', password='testpassword',first_name="a",last_name='b',date_of_birth='2003-04-12',phone_number='+375 (44) 123-45-67'
        )
        self.provider = Provider.objects.create(email="testp@gmail.com",
                                               name='testprovider',
                                               phone_number='+375 (44) 123-45-67',
                                                worker=self.user
                                               )
        self.category = ProductCategory.objects.create(name='test_category')
        self.product = Product.objects.create(id=1,name='product1', provider=self.provider, price=2, vendor_code='123')
        self.product.categories.add(self.category)

    def test_list_products(self):
        url = reverse('shop:list_products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/list_products.html')
        self.assertIn(self.product, response.context['products'])

    def test_poducts_details(self):
        url = reverse('shop:product_details', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_details.html')
        self.assertEqual(response.context['product'], self.product)

    def test_edit_product(self):
        url = reverse('shop:edit_product', args=[self.provider, self.product.id])
        with self.modify_user_is_staff(self.user, is_staff=True):
            self.client.force_login(self.user)
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'product/edit_product.html')
            self.assertEqual(response.context['product'], self.product)

    def test_delete_product(self):
        url = reverse('shop:delete_product', args=[self.product.id])
        with self.modify_user_is_staff(self.user, is_staff=True):
            self.client.force_login(self.user)
            response = self.client.post(url)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, '/')
            self.assertFalse(Product.objects.filter(id=self.product.id).exists())