import json
from django.core.management.base import BaseCommand, CommandError
from mainapp.models import Ingredient, IngredientAliasName, Hazard, WarningAgency, Source

class Command(BaseCommand):
    help = 'Imports data from list.txt into the database'

    def handle(self, *args, **options):
        with open('list.txt', 'r') as file:
            data = json.load(file)

        for item in data:
            ingredient_data = item['ingredient']
            aliases = ingredient_data.get('ingredient_alias_names', [])

            # Get or create Ingredient
            ingredient, created = Ingredient.objects.get_or_create(
                id=ingredient_data['id'],
                defaults={
                    'name': ingredient_data['name'],
                    'cas_number': ingredient_data['cas_number'],
                    'usage': ingredient_data['usage'],
                    'explanation': ingredient_data['explanation'],
                    # Add more fields as needed
                }
            )

            # Update aliases
            for alias_name in aliases:
                IngredientAliasName.objects.get_or_create(
                    ingredient=ingredient,
                    name=alias_name
                )

            # Update hazards
            for hazard in ingredient_data['hazards']:
                hazard_obj, _ = Hazard.objects.get_or_create(
                    id=hazard['id'],
                    defaults={
                        'ingredient': ingredient,
                        'name': hazard['name'],
                        'rating': hazard['rating'],
                        'benefit': hazard['benefit'],
                        # Add more fields as needed
                    }
                )
                # If the Hazard already exists, update its fields
                if not hazard_obj._state.adding:
                    hazard_obj.ingredient = ingredient
                    hazard_obj.name = hazard['name']
                    hazard_obj.rating = hazard['rating']
                    hazard_obj.benefit = hazard['benefit']
                    # Update more fields as needed
                    hazard_obj.save()

            # Update warning agencies
            for agency in ingredient_data['warning_agencies']:
                warning_agency_obj, _ = WarningAgency.objects.get_or_create(
                    id=agency['id'],
                    defaults={
                        'ingredient': ingredient,
                        'name': agency['name'],
                        'jurisdiction': agency['jurisdiction'],
                        'link': agency['link'],
                        # Add more fields as needed
                    }
                )
                # If the WarningAgency already exists, update its fields
                if not warning_agency_obj._state.adding:
                    warning_agency_obj.ingredient = ingredient
                    warning_agency_obj.name = agency['name']
                    warning_agency_obj.jurisdiction = agency['jurisdiction']
                    warning_agency_obj.link = agency['link']
                    # Update more fields as needed
                    warning_agency_obj.save()

            # Update sources
            for source in ingredient_data['sources']:
                source_obj, _ = Source.objects.get_or_create(
                    id=source['id'],
                    defaults={
                        'ingredient': ingredient,
                        'name': source['name'],
                        'link': source['link'],
                        # Add more fields as needed
                    }
                )
                # If the Source already exists, update its fields
                if not source_obj._state.adding:
                    source_obj.ingredient = ingredient
                    source_obj.name = source['name']
                    source_obj.link = source['link']
                    # Update more fields as needed
                    source_obj.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))