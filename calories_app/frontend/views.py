from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Avg
# Create your views here.
from profiles.models import Profile, TargetCalories
from profiles.forms import TargetCaloriesForm, ProfileForm
from recipe.forms import RecipeForm
from recipe.models import Recipe, Category
from planning.models import DayCalories, DayCategory, UserRecipe
from planning.models import Profile
from recipe.nutrition_helper import ask_llm, translate_to_english
from .forms import DateRangeForm
import datetime
from planning.forms import UserRecipeLLMForm
import json


@login_required(login_url='login')
def homepage(request):
    """
    This view is the homepage of the application.
    Shows summary of user data  and some statistics

    """
    page_title = "Homepage"
    profile = request.user.profile
    last_days = DayCalories.objects.filter(profile=profile)[:7]
    last_days_calories = last_days.aggregate(Sum('calories'))['calories__sum'] or 0
    this_month_qs = DayCalories.objects.filter(date__month=datetime.datetime.today().month)
    this_month_calories = this_month_qs.aggregate(Sum('calories'))['calories__sum'] or 0
    data = DayCategory.fetch_data_per_category(request.user.profile)
    
    today_data, created = DayCalories.objects.get_or_create(profile=profile,
                                                            date=datetime.datetime.today())
    target_calories, created = TargetCalories.objects.get_or_create(profile=profile)
    return render(request, "dashboard.html",
                  {
                      "profile": profile,
                      "last_days": last_days,
                      "last_days_calories": last_days_calories/7,
                      "data": data,
                      "today_data": today_data,
                      "page_title": page_title,
                      "target_calories": target_calories,
                      "this_month_calories": this_month_calories/this_month_qs.count() if this_month_qs.count() > 0 else 0  
                  }
                  )


def recipes_list_view(request):
    """
    This view is the recipes list view.
    It displays the recipes list and user can see it without login.
    """
    qs = Recipe.search_recipes(request) if request.GET.get("q") else Recipe.objects.all()[:30]
    return render(request, 'recipe_list_view.html', {"qs": qs})


@login_required(login_url='login')
def create_recipe_form_view(request):
    """
    This view is the create recipe form view.
    It displays the create recipe form and user can create a recipe.
    """
    # i want to delete the cookie after the recipe is suggested because the view will take always alot of time to load  
    #  recipe_title = request.COOKIES.get("llm_recipe", "")
    
    suggested_data = {
        "food": '',
        "calories": 0,
        "protein": 0,
        "fats": 0,
        "carbs": 0
    }
    """
    if recipe_title != "":
        recipe_title = translate_to_english(recipe_title)
        suggested_data = ask_llm(recipe_title)
        suggested_data = json.loads(suggested_data)
    """
    
      
    form = RecipeForm(request.POST or None,
                      initial={
                          "title": suggested_data["food"],
                          "calories": suggested_data["calories"],
                          "protein": suggested_data["protein"],
                          "fats": suggested_data["fats"],
                          "carbs": suggested_data["carbs"],
                          "user": request.user
                      })
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('recipe_list'))
    
    response = render(request, 'form_view.html', context={"form": form, "page_title": "Add Recipe"})
    response.delete_cookie("llm_recipe")
    return response


@login_required(login_url='login')
def today_data_view(request):

    """
    This view is the today data view.
    It displays the today data and can be modified by the user.
    """

    context = dict()
    # checks if profile exists for the logged user, if no, redirects to profile create page
    profile_qs = Profile.objects.filter(user=request.user)
    if not profile_qs.exists():
        return HttpResponseRedirect('')
 
    # fetch all the day available data for this profile
    profile = profile_qs.first()
    context['day'], created = DayCalories.objects.get_or_create(
        profile=profile,
        date=datetime.datetime.today()
    )
    context['day_categories'] = DayCategory.objects.filter(day=context['day'])
    context['categories'] = Category.objects.all()
    context['recipes'] = Recipe.objects.all()[:20]
    llm_recipe_form = UserRecipeLLMForm(request.POST or None)
    llm_recipe_form.fields['category'].queryset = DayCategory.objects.filter(day=context['day'])
    context['llm_recipe_form'] = llm_recipe_form

    return render(request, 'day_data.html', context)


@login_required(login_url='login')
def day_calories_view(request, pk):
    context = dict()
    day_calories = get_object_or_404(DayCalories, id=pk)
    if request.user.profile != day_calories.profile:
        return HttpResponseRedirect(reverse('homepage'))
    
    context['day'] = day_calories
    context['day_categories'] = DayCategory.objects.filter(day=day_calories)
    context['categories'] = Category.objects.all()
    context['recipes'] = Recipe.objects.all()[:20]


    return render(request, 'day_data.html', context)



@login_required(login_url='login')
def history_view(request):
    context = dict()
    
    # Initialize the form with request data or None
    form = DateRangeForm(request.GET or None)
    context['form'] = form
    
    # Start with base queryset
    qs = DayCalories.search_query(request)
    
    # Apply date filters if form is valid
    if form.is_valid():
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')
        
        if start_date:
            qs = qs.filter(date__gte=start_date)
        if end_date:
            qs = qs.filter(date__lte=end_date)
    
    context['qs'] = qs
    context['total_calories'] = qs.aggregate(Sum('calories'))['calories__sum'] or 0
    context['total_protein'] = qs.aggregate(Sum('protein'))['protein__sum'] or 0
    context['total_carbs'] = qs.aggregate(Sum('carbs'))['carbs__sum'] or 0
    context['total_fats'] = qs.aggregate(Sum('fats'))['fats__sum'] or 0
    
    # Calculate averages if there are records
    context['avg_calories'] = qs.aggregate(Avg('calories'))['calories__avg'] or 0
    context['avg_protein'] = qs.aggregate(Avg('protein'))['protein__avg'] or 0
    context['avg_carbs'] = qs.aggregate(Avg('carbs'))['carbs__avg'] or 0
    context['avg_fats'] = qs.aggregate(Avg('fats'))['fats__avg'] or 0


    return render(request, 'history.html', context)



@login_required(login_url='login')      
def account_view(request):
    profile = Profile.objects.get(user=request.user)
    profile_form = ProfileForm(request.POST or None, instance=profile)
    target_calories, created = TargetCalories.objects.get_or_create(profile=profile)
    target_calories_form = TargetCaloriesForm(request.POST or None, instance=target_calories)
    return render(request, 'account.html', {'profile': profile,
                                            'target_calories': target_calories,
                                            'target_calories_form': target_calories_form,
                                            'profile_form': profile_form,
                                            'page_title': 'Account'

                                      
                                            })


@login_required(login_url='login')
def statistics_view(request):
    user = request.user
    day_calories = DayCalories.objects.filter(profile=user.profile)

    foods_analysis = UserRecipe.objects.filter(
        day_calories = day_calories
    ).annotate(
        avg_protein = Avg('protein'),
        avg_calories = Avg('calories')
    ).values(
        'recipe__title',
        'avg_protein',
        'avg_calories'
    ).order_by('recipe__title')
    context = locals()
    return render(request, '', context)