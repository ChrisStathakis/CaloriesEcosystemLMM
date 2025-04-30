from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required

from planning.models import DayCalories, DayCategory, UserRecipe
from recipe.models import Category, Recipe
from planning.forms import UserRecipeForm
from recipe.nutrition_helper import ask_llm, get_nutrition_info, string_to_list, translate_to_english
from profiles.forms import ProfileForm, TargetCaloriesForm
from profiles.models import Profile, TargetCalories

import decimal

@login_required
def create_day_category_view(request, pk, dk):
    day_calories = get_object_or_404(DayCalories, id=pk)
    category = get_object_or_404(Category, id=dk)
    day_category, created = DayCategory.objects.get_or_create(
        category=category,
        day=day_calories
    )
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required
def add_recipe_to_day_view(request, pk, dk,):
    context = dict()
    recipe = get_object_or_404(Recipe, id=dk)
    day = get_object_or_404(DayCalories, id=pk)

    form = UserRecipeForm(request.POST or None, initial={
        'recipe': recipe,
        'day_calories': day,
    })
    form.fields['category'].queryset = DayCategory.objects.filter(day=day)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(day.get_absolute_url())

    context['recipe'], context['day'], context['form'] = recipe, day, form
    return render(request, 'action/add_recipe_to_day.html', context)



@login_required
def edit_user_recipe_view(request, pk):
    user_recipe = get_object_or_404(UserRecipe, id=pk)
    if request.user.profile != user_recipe.day_calories.profile:
        return HttpResponseRedirect(user_recipe.day_calories.get_absolute_url())

    form = UserRecipeForm(request.POST or None, instance=user_recipe)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(user_recipe.day_calories.get_absolute_url())
    context = dict()
    context['form'] = form
    context['delete_button'] = True
    context['delete_url'] = reverse('delete_user_recipe', kwargs={'pk': user_recipe.id})
    context['day'] = user_recipe.day_calories
    context['recipe'] = user_recipe.recipe
    return render(request, 'action/add_recipe_to_day.html', context)


@login_required
def delete_user_recipe_view(request, pk):
    user_recipe = get_object_or_404(UserRecipe, id=pk)
    if request.user.profile != user_recipe.day_calories.profile:
        return HttpResponseRedirect(user_recipe.day_calories.get_absolute_url())
    user_recipe.delete()
    return HttpResponseRedirect(reverse("today_data"))


@login_required
def analyze_food_view(request, pk):
    day = get_object_or_404(DayCalories, id=pk)
    sentence = request.GET.get('food')
    sentence = translate_to_english(sentence)
    category = get_object_or_404(DayCategory, id=request.GET.get('category'))
    result = get_nutrition_info(sentence)
    food_list = string_to_list(result)
    suggested_foods = dict()
    for food in food_list:
        qs = Recipe.objects.filter(title__icontains=food[0])
        suggested_foods[food[0]] = [qs, food[1]]

    return render(request, 'action/analyze_food.html', {'day': day, 
                                                        'result': result, 
                                                        'sentence': sentence,
                                                        "suggested_foods": suggested_foods,
                                                        "category": category
                                                        },
                                                        )

@login_required
def add_recipe_to_day_llm_view(request, pk, dk, qty):
    recipe = get_object_or_404(Recipe, id=pk)
    day_category = get_object_or_404(DayCategory, id=dk)
    user_recipe = UserRecipe.objects.create(
        recipe = recipe,
        day_calories = day_category.day,
        category = day_category,
        qty = qty
    )
    return HttpResponseRedirect(reverse('today_data'))

@login_required
def create_recipe_llm_view(request, pk, dk, fk):
    day_clories = get_object_or_404(DayCalories, id=pk)
    day_category = get_object_or_404(DayCategory, id=fk)
    if request.user.profile != day_clories.profile:
        return HttpResponseRedirect(reverse('today_data'))
    recipe = get_object_or_404(Recipe, id=dk)
    qty = request.GET.get('qty', 1)
    if type(qty) != str:
       return HttpResponseRedirect(reverse('today_data'))

    new_recipe = UserRecipe.objects.create(
        recipe = recipe,
        day_calories = day_clories,
        category = day_category,
        qty = decimal.Decimal(qty)
    )
    return HttpResponseRedirect(reverse('today_data'))
    
    

@login_required
def handle_profile_form_view(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return HttpResponseRedirect(reverse('account'))
    return HttpResponseRedirect(reverse('account'))


@login_required
def handle_target_calories_form_view(request):
    target_calories = TargetCalories.objects.get(profile=request.user.profile)
    if request.method == 'POST':
        target_calories_form = TargetCaloriesForm(request.POST, instance=target_calories)
        if target_calories_form.is_valid():
            target_calories_form.save()
            return HttpResponseRedirect(reverse('account'))
    return HttpResponseRedirect(reverse('account'))
        


def ask_llm(request):
    food = request.GET.get('q', '')
    result = ask_llm(food)
    print(result)