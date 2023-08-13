from django.test import TestCase, Client
from django.urls import reverse
from .models import Ingredient, Image
from .views import HomeView, IngredientListView, IngredientDetailView


class HomeViewTestCase(TestCase):
    def test_home_view(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        print("Тест test_home_view выполнен успешно, ошибок не обнаружено")


class IngredientListViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse('ingredient_list')

    def test_ingredient_list_view(self):
        client = Client()
        response = client.get(self.url)
        self.assertEqual(response.status_code, 200)
        print("Тест test_ingredient_list_view выполнен успешно, ошибок не обнаружено")

    def test_ingredient_list_context(self):
        ingredient = Ingredient.objects.create(name='Test Ingredient')
        client = Client()
        response = client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('ingredients', response.context)
        ingredients = response.context['ingredients']
        self.assertIn(ingredient, ingredients)
        print("Тест test_ingredient_list_context выполнен успешно, ошибок не обнаружено")


class IngredientDetailViewTestCase(TestCase):
    def setUp(self):
        self.ingredient = Ingredient.objects.create(name='Test Ingredient')
        self.url = reverse('ingredient_detail', args=[self.ingredient.pk])

    def tearDown(self):
        self.ingredient.delete()

    def test_ingredient_detail_view(self):
        client = Client()
        response = client.get(self.url)
        self.assertEqual(response.status_code, 200)
        print("Тест test_ingredient_detail_view выполнен успешно, ошибок не обнаружено")

    def test_ingredient_detail_context(self):
        client = Client()
        response = client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('ingredient', response.context)
        ingredient = response.context['ingredient']
        self.assertEqual(ingredient, self.ingredient)
        print("Тест test_ingredient_detail_context выполнен успешно, ошибок не обнаружено")

    def test_ingredient_detail_back_button(self):
        client = Client()
        response = client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'href="/ingredients/"')
        print("Тест test_ingredient_detail_back_button выполнен успешно, ошибок не обнаружено")