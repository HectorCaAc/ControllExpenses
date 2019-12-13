from django.test import TestCase
from django.contrib.auth.models import User

from account.models import CustomUser
from expenses.models import Category, Entry


class CategoryTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="test_db")
        Category.objects.create(user=self.user,
                                expense = 100,
                                circle_repetition = 30,
                                spend_available = 100 )
        CustomUser.objects.create(user=self.user,
                                current_balance= 100)

    def test_new_category(self):
        user_category = Category.objects.get(user= self.user)
        self.assertFalse(user_category.deficit)
        self.assertEqual(100, user_category.spend_available)

    def test_add_entry(self):
        user_category = Category.objects.get(user= self.user)
        Entry.objects.create(user=self.user,
                            category=user_category,
                            price =50)
        self.assertEqual(50, user_category.spend_available)
        self.assertFalse(user_category.deficit)

    def test_category_overload(self):
        pass

    def test_try_to_add_negative_value(self):
        pass
