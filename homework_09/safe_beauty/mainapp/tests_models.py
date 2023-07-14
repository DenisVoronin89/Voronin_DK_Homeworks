from django.test import TestCase
from django.utils import timezone
from .models import (
    Ingredient,
    IngredientAliasName,
    Hazard,
    WarningAgency,
    Source,
    Image,
)


class IngredientModelTestCase(TestCase):
    def setUp(self):
        self.ingredient_data = {
            'name': 'Test Ingredient',
            'cas_number': '12345-67-8',
        }
        self.ingredient = Ingredient.objects.create(**self.ingredient_data)

    def tearDown(self):
        self.ingredient.delete()

    def test_str_representation(self):
        self.assertEqual(str(self.ingredient), self.ingredient_data['name'])
        print("Тест test_str_representation для модели Ingredient выполнен успешно, ошибок не обнаружено")


class IngredientAliasNameModelTestCase(TestCase):
    def setUp(self):
        self.ingredient = Ingredient.objects.create(name='Test Ingredient')
        self.alias_name = 'Alias Name'
        self.ingredient_alias_name = IngredientAliasName.objects.create(
            ingredient=self.ingredient,
            name=self.alias_name
        )

    def tearDown(self):
        self.ingredient_alias_name.delete()
        self.ingredient.delete()

    def test_str_representation(self):
        self.assertEqual(str(self.ingredient_alias_name), self.alias_name)
        print("Тест test_str_representation для модели IngredientAliasName выполнен успешно, ошибок не обнаружено")


class HazardModelTestCase(TestCase):
    def setUp(self):
        self.ingredient = Ingredient.objects.create(name='Test Ingredient')
        self.hazard_data = {
            'name': 'Test Hazard',
            'rating': 5,
        }
        self.hazard = Hazard.objects.create(
            ingredient=self.ingredient,
            **self.hazard_data
        )

    def tearDown(self):
        self.hazard.delete()
        self.ingredient.delete()

    def test_str_representation(self):
        self.assertEqual(str(self.hazard), self.hazard_data['name'])
        print("Тест test_str_representation для модели Hazard выполнен успешно, ошибок не обнаружено")


class WarningAgencyModelTestCase(TestCase):
    def setUp(self):
        self.ingredient = Ingredient.objects.create(name='Test Ingredient')
        self.warning_agency_data = {
            'name': 'Test Warning Agency',
            'jurisdiction': 'Test Jurisdiction',
        }
        self.warning_agency = WarningAgency.objects.create(
            ingredient=self.ingredient,
            **self.warning_agency_data
        )

    def tearDown(self):
        self.warning_agency.delete()
        self.ingredient.delete()

    def test_str_representation(self):
        self.assertEqual(str(self.warning_agency), self.warning_agency_data['name'])
        print("Тест test_str_representation для модели WarningAgency выполнен успешно, ошибок не обнаружено")


class SourceModelTestCase(TestCase):
    def setUp(self):
        self.ingredient = Ingredient.objects.create(name='Test Ingredient')
        self.source_data = {
            'name': 'Test Source',
            'link': 'http://example.com',
        }
        self.source = Source.objects.create(
            ingredient=self.ingredient,
            **self.source_data
        )

    def tearDown(self):
        self.source.delete()
        self.ingredient.delete()

    def test_str_representation(self):
        self.assertEqual(str(self.source), self.source_data['name'])
        print("Тест test_str_representation для модели Source выполнен успешно, ошибок не обнаружено")


class ImageModelTestCase(TestCase):
    def setUp(self):
        self.image_data = {
            'title': 'Test Image',
        }
        self.image = Image.objects.create(**self.image_data)

    def tearDown(self):
        self.image.delete()

    def test_str_representation(self):
        self.assertEqual(str(self.image), self.image_data['title'])
        print("Тест test_str_representation для модели Image выполнен успешно, ошибок не обнаружено")