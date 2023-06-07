from django.shortcuts import render

from .models import Ingredient, IngredientAliasName, Hazard, WarningAgency, Source

def index_view(request):
    ingredients = Ingredient.objects.all()
    sources = Source.objects.all()
    return render(request, 'mainapp/index.html', {'ingredients': ingredients, 'sources': sources})