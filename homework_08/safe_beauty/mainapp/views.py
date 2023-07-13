from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Ingredient, Image


def index_view(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'mainapp/ingredient_list.html', {'ingredients': ingredients})


class HomeView(TemplateView):
    template_name = 'mainapp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        images = Image.objects.all()
        context['images'] = images
        return context


class IngredientListView(ListView):
    model = Ingredient
    template_name = 'mainapp/ingredient_list.html'
    context_object_name = 'ingredients'
    ordering = ['name']  # Сортировка по имени


class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = 'mainapp/ingredient_detail.html'
    context_object_name = 'ingredient'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ingredient = self.object

        # Получаем все связанные источники для данного ингредиента
        sources = ingredient.sources.all()

        context['sources'] = sources
        return context