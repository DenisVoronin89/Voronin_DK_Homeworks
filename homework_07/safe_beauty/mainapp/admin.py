from django.contrib import admin

from .models import Ingredient, IngredientAliasName, Hazard, WarningAgency, Source


admin.site.register(Ingredient)
admin.site.register(IngredientAliasName)
admin.site.register(Hazard)
admin.site.register(WarningAgency)
admin.site.register(Source)