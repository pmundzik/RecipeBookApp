# Generated by Django 3.0.6 on 2020-05-07 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=255)),
                ('prepare_time', models.IntegerField()),
                ('portion', models.IntegerField()),
                ('image_url', models.CharField(max_length=2083)),
                ('recipe_url', models.CharField(default='', max_length=2083)),
                ('type_of_meal', models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('soup', 'Soup'), ('dessert', 'Dessert'), ('salad', 'Salad')], default='dinner', max_length=9)),
            ],
        ),
    ]
