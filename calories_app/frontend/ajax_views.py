from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from recipe.models import Recipe
from planning.models import DayCalories
from recipe.nutrition_helper import translate_to_english
from recipe.nutrition_helper import ask_llm, translate_to_english

def ajax_search_recipes(request, pk):
    selected_day = get_object_or_404(DayCalories, id=pk)
    search_query = request.GET.get('q', '')
    q = translate_to_english(search_query)
    print("tranlated q", q)
    
    data, qs = dict(), Recipe.objects.none()
    qs = Recipe.search_recipes(request)[:10]
    data['result'] = render_to_string(
        template_name='ajax_views/recipe_search.html',
        request=request,
        context={
            'recipes': qs,
            'day': selected_day,
            'search_query': search_query
        }
    )

    return JsonResponse(data)

def ajax_suggest_food_view(request):
    q = request.GET.get('q', '')
    result = ask_llm(q)
    print(result)