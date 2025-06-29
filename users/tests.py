from django.test import TestCase
from django.test import Client
from users.models import User
# Create your tests here.
class TestUsers(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email='test@example.com', password='PyTests426$',username='test')

    def test_01_register_user(self):
        post_data ={
            'email':'tester@example.com',
            'password1':'TestParol1',
            'password2':'TestParol1',
            'username':'test'

        }
        response = self.client.get('/users/register/')
        self.assertEqual(response.status_code,200)
        response = self.client.post('/users/register/',post_data)
        self.assertEqual(response.status_code,302)


    def test_02_login_user(self):
        post_data = {
            'username':self.user.email,
            'password':'PyTests426$',
        }
        response = self.client.get('/users/user_login/')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/users/user_login/', post_data)
        self.assertEqual(response.status_code, 302)

    def test_03_profile_user(self):
        self.client.login(email='test@example.com', password='PyTests426$')
        response = self.client.get('/users/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user'].username, 'test')

    def test_04_profile_update(self):
        post_data = {
            'email': 'tester@example.com',

            'username': 'test',
            'phone': "+1(333)21-445-32"
        }

        self.client.login(email='test@example.com', password='PyTests426$')

        response = self.client.post('/users/update/',post_data)
        self.assertEqual(response.status_code,302)
        self.user.refresh_from_db()
        response = self.client.get('/users/profile/')
        self.assertEqual(response.context['user'].phone, '+1(333)21-445-32')

    def test_05_change_password(self):
        post_data = {
            'old_password': 'PyTests426$',
            'new_password1': 'Tester24333',
            'new_password2': 'Tester24333',


        }
        self.client.login(email='test@example.com', password='PyTests426$')
        response = self.client.get('/users/change_password/')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/users/change_password/', post_data)

        self.assertEqual(response.status_code, 302)

    def test_06_logout(self):
        self.client.login(email='test@example.com', password='PyTests426$')


        response = self.client.post('/users/logout/')
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'users/user_logout.html')