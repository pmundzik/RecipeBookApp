from django.contrib import admin
from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe_name', 'type_of_meal', 'prepare_time', 'portion')


admin.site.register(Recipe, RecipeAdmin)
