from django.db import models


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255)
    prepare_time = models.IntegerField()
    portion = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    recipe_url = models.CharField(max_length=2083, default="")
    type_of_meal_choices = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('soup', 'Soup'),
        ('dessert', 'Dessert'),
        ('salad', "Salad"),
    ]
    type_of_meal = models.CharField(
        max_length=9,
        choices=type_of_meal_choices,
        default='dinner',
    )
