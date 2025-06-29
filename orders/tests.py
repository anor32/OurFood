from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.http import HttpResponseForbidden
from unittest.mock import patch

from unicodedata import category

from orders.models import Order, OrderProduct
from products.models import Product, Category, ParentCategory  # предположим, что Product в products.models

User = get_user_model()

class TestOrders(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(email='test@example.com', password='PyTests426', username='testuser')


        self.parent = ParentCategory.objects.create(id=5, name='test_ParentCategory')
        self.category = Category.objects.create(id=2, name="test_Category", parent_category=self.parent)
        self.sales = Category.objects.create(id=28, name="test_Category", parent_category=self.parent)
        self.product1 = Product.objects.create(id=3, name='test_Product', categoryID=self.category, price=100,
                                              original_price=100, quantity=10)

        self.product2 = Product.objects.create(id=4,name='Product2', price=200,original_price=200, quantity=5,categoryID=self.category)


        self.create_url = reverse('orders:cart_order')
        self.list_url = reverse('orders:order_panel')
        self.success_url = reverse('orders:success_payment')
        self.order_panel_url = reverse('orders:order_panel')


        self.client.login(email='test@example.com', password='PyTests426')

    def test_01_order_create_get(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'payment_page.html')

    def test_02_order_create_post_empty_cart(self):
        session = self.client.session
        session['cart'] = []
        session.save()

        response = self.client.post(self.create_url)
        self.assertEqual(response.status_code, 403)

    def test_03_order_create_post_invalid_card_data(self):

        session = self.client.session
        session['cart'] = [
            {'id': self.product1.id, 'price': self.product1.price, 'quantity': 1},
            {'id': self.product2.id, 'price': self.product2.price, 'quantity': 2},
        ]
        session.save()


        post_data = {
            'card-name': 'Invalid Name',
            'card-expiration': '00/00',
            'card-number': '123',
            'card-ccv': '12',
        }


        with patch('orders.views.valid_name_card', side_effect=ValidationError('Invalid name')):
            with patch('orders.views.valid_date', side_effect=ValidationError('Invalid date')):
                with patch('orders.views.valid_number_card', side_effect=ValidationError('Invalid number')):
                    with patch('orders.views.valid_cvv', side_effect=ValidationError('Invalid cvv')):
                        response = self.client.post(self.create_url, post_data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'payment_page.html')
        self.assertIn('errors', response.context)
        self.assertTrue(len(response.context['errors']) > 0)

    def test_04_order_create_post_success(self):
        # Устанавливаем корзину в сессии
        session = self.client.session
        session['cart'] = [
            {'id': self.product1.id, 'price': self.product1.price, 'quantity': 1},
            {'id': self.product2.id, 'price': self.product2.price, 'quantity': 2},
        ]
        session.save()

        post_data = {
            'card-name': 'Valid Name',
            'card-expiration': '12/25',
            'card-number': '1234567890123456',
            'card-ccv': '123',
        }

        with patch('orders.views.valid_name_card', return_value=None), \
                patch('orders.views.valid_date', return_value=None), \
                patch('orders.views.valid_number_card', return_value=None), \
                patch('orders.views.valid_cvv', return_value=None), \
                patch('orders.views.to_json') as mock_to_json:
            response = self.client.post(self.create_url, post_data)

        self.assertRedirects(response, self.success_url)

        # Получаем созданный заказ
        order = Order.objects.filter(order_user=self.user).last()
        self.assertIsNotNone(order)

        # Проверяем totalSum
        expected_sum = self.product1.price * 1 + (self.product2.price * 2)
        self.assertEqual(order.totalSum, expected_sum)

        # Проверяем, что созданы и связаны OrderProduct
        order_products = order.products.all()
        self.assertEqual(order_products.count(), 2)

        op1 = order_products.get(product=self.product1)
        self.assertEqual(op1.quantity, 1)

        op2 = order_products.get(product=self.product2)
        self.assertEqual(op2.quantity, 2)

        # Проверяем уменьшение количества продуктов
        self.product1.refresh_from_db()
        self.product2.refresh_from_db()
        self.assertEqual(self.product1.quantity, 9)  # 10 - 1
        self.assertEqual(self.product2.quantity, 3)  # 5 - 2

        # Проверяем очистку корзины в сессии
        session = self.client.session
        self.assertEqual(session.get('cart'), [])



    def test_05_order_list_view(self):

        Order.objects.create(order_user=self.user, totalSum=100)
        Order.objects.create(order_user=self.user, totalSum=200)

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orderPanel.html')
        self.assertEqual(len(response.context['order_list']), 2)

    def test_06_order_delete_view(self):

            op = OrderProduct.objects.create(product=self.product1, quantity=1)
            order = Order.objects.create(order_user=self.user, totalSum=100)
            order.products.add(op)

            delete_url = reverse('orders:order_delete', kwargs={'pk': order.pk})

            # Отправляем POST-запрос на удаление
            response = self.client.post(delete_url)

            # Проверяем редирект на панель заказов
            self.assertRedirects(response, self.order_panel_url)

            # Проверяем, что заказ удалён
            self.assertFalse(Order.objects.filter(pk=order.pk).exists())

    def test_07_order_success_view(self):
        url = reverse('orders:success_payment')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'success_payment.html')
