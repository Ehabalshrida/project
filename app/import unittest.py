import unittest
from django.urls import reverse, resolve
from . import views

class TestUrls(unittest.TestCase):
    def test_home_url(self):
        url = reverse('app:home')
        resolved = resolve(url)
        self.assertEqual(resolved.func, views.homeTemplate)

    def test_about_url(self):
        url = reverse('app:about')
        resolved = resolve(url)
        # For class-based views, resolved.func.view_class is the class
        self.assertEqual(resolved.func.view_class, views.AboutTemplate)

    def test_users_url(self):
        url = reverse('app:users')
        resolved = resolve(url)
        self.assertEqual(resolved.func, views.users)

    def test_add_user_url(self):
        url = reverse('app:addUser')
        resolved = resolve(url)
        self.assertEqual(resolved.func, views.addUser)

    def test_delete_user_url(self):
        url = reverse('app:deleteUser')
        resolved = resolve(url)
        self.assertEqual(resolved.func, views.deleteUser)

    def test_form_url(self):
        url = reverse('app:form')
        resolved = resolve(url)
        self.assertEqual(resolved.func.view_class, views.UserModelFormView)