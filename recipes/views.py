from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe


def index(request):
    # recipes = Recipe.objects.all()
    return render(request, 'index.html')


def all_recipes(request):
    recipes = Recipe.objects.all()
    if recipes:
        return render(request, 'recipe_card.html', {'recipes': recipes})
    else:
        return render(request, 'no_recipes.html')


def all_breakfasts(request):
    breakfasts = Recipe.objects.filter(type_of_meal="breakfast")
    if breakfasts:
        return render(request, 'recipe_card.html', {'recipes': breakfasts})
    else:
        return render(request, 'no_recipes.html')


def all_lunches(request):
    lunches = Recipe.objects.filter(type_of_meal="lunch")
    if lunches:
        return render(request, 'recipe_card.html', {'recipes': lunches})
    else:
        return render(request, 'no_recipes.html')


def all_salads(request):
    salads = Recipe.objects.filter(type_of_meal="salad")
    if salads:
        return render(request, 'recipe_card.html', {'recipes': salads})
    else:
        return render(request, 'no_recipes.html')


def all_dinners(request):
    dinners = Recipe.objects.filter(type_of_meal="dinner")
    if dinners:
        return render(request, 'recipe_card.html', {'recipes': dinners})
    else:
        return render(request, 'no_recipes.html')


def all_soups(request):
    soups = Recipe.objects.filter(type_of_meal="soup")
    if soups:
        return render(request, 'recipe_card.html', {'recipes': soups})
    else:
        return render(request, 'no_recipes.html')


def all_desserts(request):
    desserts = Recipe.objects.filter(type_of_meal="dessert")
    if desserts:
        return render(request, 'recipe_card.html', {'recipes': desserts})
    else:
        return render(request, 'no_recipes.html')


def favourites(request):
    favourite_recipes_list = Recipe.objects.all()
    context = {'favourite_recipes_list': favourite_recipes_list}
    if favourite_recipes_list:
        return render(request, 'favourites.html', context)
    else:
        return render(request, 'no_recipes.html')


def new_recipe(request):
    return HttpResponse('New Recipe')
