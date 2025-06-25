from django.test import TestCase
from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(title="first", price="1.00")
        self.item2 = Menu.objects.create(title="second", price="2.00")

    def test_getall(self):
        first = Menu.objects.get(title="first")
        second = Menu.objects.get(title="second")

        self.assertEqual(str(first), "first : 1.00")
        self.assertEqual(str(second), "second : 2.00")
