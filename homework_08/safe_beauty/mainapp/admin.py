from django.contrib import admin

from .models import Ingredient, IngredientAliasName, Hazard, WarningAgency, Source, Image


admin.site.register(Ingredient)
admin.site.register(IngredientAliasName)
admin.site.register(Hazard)
admin.site.register(WarningAgency)
admin.site.register(Source)
admin.site.register(Image)