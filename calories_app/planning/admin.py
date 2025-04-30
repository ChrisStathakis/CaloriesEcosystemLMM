from django.contrib import admin
from .models import DayCalories, DayCategory, UserRecipe


@admin.register(DayCategory, UserRecipe, DayCalories)
class DayCategoryAdmin(admin.ModelAdmin):
    pass



