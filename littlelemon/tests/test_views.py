from django.test import TestCase
from django.contrib.auth.models import User
from restaurant.views import Menu
from restaurant.serializers import MenuItemSerializer
from rest_framework import status
from django.urls import reverse


# test the list and create functionality of the MenuView API endpoint (/menu/)
class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.force_login(self.user)
        # Create three test Menu Items
        Menu.objects.create(title = "Kuskus", price = 7.50, inventory = 50)
        Menu.objects.create(title = "Thaicurry", price = 12.50, inventory = 25)
        Menu.objects.create(title = "Rice and Beans", price = 15.50, inventory = 10)

    def test_getall(self):
        menu_items = Menu.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        response = self.client.get(reverse('menu-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    