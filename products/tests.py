
from django.test import TestCase


from products.models import Product, Category, ParentCategory

from users.models import User


# Create your tests here.

class TestProducts(TestCase):
    def setUp(self):
        self.parent = ParentCategory.objects.create(id=5, name='test_ParentCategory')
        self.category = Category.objects.create(id=2, name="test_Category", parent_category=self.parent)
        self.sales = Category.objects.create(id=28, name="test_Category", parent_category=self.parent)
        self.product = Product.objects.create(id=2, name='test_Product', categoryID=self.category, price=100,
                                              original_price=100,quantity=10)

        admin_user = User.objects.create(
            email="admin@web.top",
            first_name="Andrei",
            last_name="Nikanov",
            role='admin',
            is_staff=True,
            is_superuser=True,
            is_active=True,

        )
        admin_user.set_password("querty")
        admin_user.save()
        self.client.login(email='admin@web.top', password='querty')


    def test_01_index_view(self):
        response = self.client.get('//')
        self.assertEqual(response.status_code, 200)

    def test_02_categories_list(self):
        url = '/products/5/categories/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        categories = response.context['objects_list']
        self.assertIn(self.category, categories)
        for cat in categories:
            self.assertEqual(cat.parent_category_id, 5)
        self.assertEqual(response.context['title'], self.parent.name)
        products = response.context['products_list']
        self.assertIn(self.product, products)
        for prod in products:
            self.assertIn(prod.categoryID, categories)
        self.assertTemplateUsed(response, 'products/categories.html')

    def test_03_parent_category_change(self):
        post_data = {
            'name': 'Updated Test Parent Category',
            'priority': 0
        }

        response = self.client.get('/product/5/change')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/product/5/change', post_data)
        self.assertEqual(response.status_code, 302)

    def test_04_parent_category_create(self):
        post_data = {
            'name': 'Created Test Parent Category',
            'priority': 0
        }

        response = self.client.get('/products/create')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/products/create'
                                    '', post_data)
        self.assertEqual(response.status_code, 302)

    def test_05_parent_category_delete(self):

        parent = ParentCategory.objects.create(id=6, name='test_ParentCategory')
        response = self.client.post(f'/products/delete/{parent.id}/')
        self.assertEqual(response.status_code, 302)

    def test_06_category_create(self):
        post_data = {
            'name': 'Created Test Category',
            'priority': 0,
            'parent_category': self.parent.id,
            'has_slider': False,
            'products': [2, ]
        }
        response = self.client.get('/products/create/category')

        self.assertEqual(response.status_code, 200)
        response = self.client.post('/products/create/category', post_data)

        self.assertEqual(response.status_code, 302)

    def test_07_category_update(self):
        post_data = {
            'name': 'Created Category',
            'priority': 30,
            'parent_category': self.parent.id,
            'has_slider': True,
            'products': [2, ]
        }

        response = self.client.get(f'/products/update/{self.category.id}/category')

        self.assertEqual(response.status_code, 200)
        response = self.client.post(f'/products/update/{self.category.id}/category', post_data)
        self.assertEqual(response.status_code, 302)

    def test_08_category_delete(self):
        category = Category.objects.create(id=3, name="test_Category", parent_category=self.parent)
        response = self.client.post(f'/products/delete/{category.id}/category')
        self.assertEqual(response.status_code, 302)

    def test_09_product_create(self):

        post_data = {
            'name': 'Test Product',
            'categoryID': self.category.id,
            'price': '150.00',
            'quantity': '10',
            'description': 'Test description',
            'barcode': '1234567890',
            'priority': '1',
            'discount': '5',
            'original_price': '160.00',
            'composition': 'Test composition',
        }
        product_ids = list(self.sales.products.values_list('id', flat=True))
        self.assertEqual(product_ids, [])
        response = self.client.post(f'/products/create/product', post_data)

        self.assertEqual(response.status_code, 302)
        product_ids = list(self.sales.products.values_list('id', flat=True))
        self.assertEqual(product_ids, [1])

    def test_10_product_detail(self):
        response = self.client.get(f'/product/{self.product.id}/detail/product')
        self.assertEqual(response.status_code, 200)

    def test_11_product_delete(self):
        product = Product.objects.create(
            id=3, name='test_Product',
            categoryID=self.category,
            price=100, original_price=100)

        response = self.client.post(f'/product/{product.id}/delete/product')
        self.assertEqual(response.status_code, 302)

    def test_12_product_update(self):

        post_data = {
            'name': 'Test Product',
            'categoryID': self.category.id,
            'price': '150.00',
            'quantity': '10',
            'description': 'Test description',
            'barcode': '1234567890',
            'priority': '1',
            'discount': '40',
            'original_price': '160.00',
            'composition': 'Test composition',
        }
        #cписок пустой
        product_ids = list(self.sales.products.values_list('id', flat=True))
        self.assertEqual(product_ids, [])

        response = self.client.get(f'/products/{self.product.id}/update/product')
        self.assertEqual(response.status_code, 200)

        #добавление в категорию скидок
        response = self.client.post(f'/products/{self.product.id}/update/product', post_data)
        self.product.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.product.price,96)
        #проверка что добавилось
        product_ids = list(self.sales.products.values_list('id', flat=True))
        self.assertEqual(product_ids, [self.product.id])

        post_data = {
            'name': 'Test Product',
            'categoryID': self.category.id,
            'price': '150.00',
            'quantity': '10',
            'description': 'Test description',
            'barcode': '1234567890',
            'priority': '1',
            'discount': '0',
            'original_price': '160.00',
            'composition': 'Test composition',
        }
        response = self.client.post(f'/products/{self.product.id}/update/product', post_data)
        self.product.refresh_from_db()
        self.assertEqual(self.product.price, 150)
        self.assertEqual(response.status_code, 302)
        product_ids = list(self.sales.products.values_list('id', flat=True))
        self.assertEqual(product_ids, [])

    def test_13_product_choice(self):

        self.client.session['cart'] = []
        self.client.session.modified = True

        response = self.client.post(f'/product/{self.product.id}/choice/product')
        self.assertEqual(response.status_code, 302)


        cart = self.client.session.get('cart', [])
        self.assertEqual(len(cart), 1)
        self.assertEqual(cart[0]['quantity'], 1)

        # Second request to add the product again
        response = self.client.post(f'/product/{self.product.id}/choice/product')
        self.assertEqual(response.status_code, 302)


        cart = self.client.session.get('cart', [])
        self.assertEqual(len(cart), 1)
        self.assertEqual(cart[0]['quantity'], 2)
        self.assertEqual(cart[0]['price'], 200)

    def test_14_product_remove(self):
        self.client.session['cart'] = []
        self.client.session.modified = True

        response = self.client.post(f'/product/{self.product.id}/choice/product')
        self.assertEqual(response.status_code, 302)

        cart = self.client.session.get('cart', [])
        self.assertEqual(cart[0]['quantity'], 1)


        response = self.client.post(f'/product/{self.product.id}/choice/product')
        self.assertEqual(response.status_code, 302)

        cart = self.client.session.get('cart', [])

        self.assertEqual(cart[0]['quantity'], 2)
        self.assertEqual(cart[0]['price'], 200)


        response = self.client.post(f'/product/{self.product.id}/remove/product')
        self.assertEqual(response.status_code, 302)
        cart = self.client.session.get('cart', [])
        self.assertEqual(cart[0]['quantity'], 1)
        self.assertEqual(cart[0]['price'], 100)


    def test_15_cart_clear(self):
        response = self.client.post(f'/product/{self.product.id}/choice/product')
        cart = self.client.session.get('cart', )

        self.assertEqual(cart,[{
               'id': 2,
              'img': '',
              'name': 'test_Product',
             'original_price': 100,
              'price': 100,
              'quantity': 1}])
        self.assertEqual(response.status_code, 302)
        response = self.client.post(f'/product/clear/')
        self.assertEqual(response.status_code, 302)
        cart = self.client.session.get('cart', )
        self.assertEqual(cart,[])

    def test_16_search_product(self):

        response = self.client.get('/products/search/results?q=test_Product')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products_results.html')

        products = response.context['object_list']
        self.assertIn(self.product, products)

        self.assertEqual(response.context['title'], 'Результаты поискового запроса')
