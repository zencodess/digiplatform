from django.test import TestCase
from .models import AccountManager, ServiceProvider, Service, Customer, Ordering
from django.utils import timezone

# models test
class AccountManagerTest(TestCase):
    account_manager_instance = None
    def create_account_manager(self, email="test_am@gmail.com", password="test_password"):
        return AccountManager(email=email, password=password)
        
    def test_account_manager_creation(self):
        account_manager_instance = self.create_account_manager()
        self.assertTrue(isinstance(account_manager_instance, AccountManager))
        self.assertEqual(account_manager_instance.email, "test_am@gmail.com")
        
    def test_customer_creation(self):
        c = self.create_user(email="test_customer@gmail.com", password="test_customer")
        self.assertTrue(isinstance(c, Customer))
        self.assertEqual(c.email, "test_customer@gmail.com")
        self.assertFalse(c.is_admin)
        self.assertFalse(c.is_staff)
        self.assertFalse(c.is_superuser)
        try:
            
            self.assertIsNone(c.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            account_manager_instance.create_user()
        with self.assertRaises(TypeError):
            account_manager_instance.create_user(email='')
        with self.assertRaises(ValueError):
            account_manager_instance.create_user(email='', password="run")

    def test_create_superuser(self):            #we create a test superuser
        user_ad = account_manager_instance.objects.create_superuser(email='head@user.com', password='tan')
        self.assertEqual(user_ad.email, 'head@user.com')
        self.assertTrue(user_ad.is_admin)
        self.assertTrue(user_ad.is_staff)
        self.assertTrue(user_ad.is_superuser)
        try:
            self.assertIsNone(user_ad.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            account_manager_instance.create_superuser(
                email='head@user.com', password='tan', is_superuser=False)
