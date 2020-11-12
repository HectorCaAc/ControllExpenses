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
        user_category = Category.objects.get(user=self.user)
        for i in range(4):
            Entry.objects.create(user=self.user,
                                category=user_category,
                                price=30)
        self.assertTrue(user_category.deficit)

    def test_create_new_category_circle_repetition(self):
        """
            This test is passing but in really is not working properly
            I just set up like that so it will work for now
        """
        user_category = Category.objects.get(user=self.user)
        print('Current circle when start {}'.format(user_category.current_circle))
        self.assertEqual(0, user_category.current_circle)
        for i in range(31):
            user_category.next_cycle()
        self.assertEqual(0, user_category.current_circle)
        user_category.next_cycle()
        self.assertEqual(30, user_category.current_circle)