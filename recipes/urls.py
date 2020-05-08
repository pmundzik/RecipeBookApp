from django.urls import path
from . import views  # from the current folder I import view folder

urlpatterns = [
    path('', views.index),

    path('recipes', views.all_recipes),
    path('recipes/breakfast', views.all_breakfasts),
    path('recipes/lunch', views.all_lunches),
    path('recipes/salad', views.all_salads),
    path('recipes/dinner', views.all_dinners),
    path('recipes/soup', views.all_soups),
    path('recipes/dessert', views.all_desserts),

    path('new', views.new_recipe)
]