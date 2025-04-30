"""calories_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

from rest_framework_simplejwt import views as jwt_views

from frontend.views import (homepage, recipes_list_view, create_recipe_form_view, today_data_view, history_view,
                            account_view, day_calories_view, statistics_view
                            )

from frontend.action_views import (create_day_category_view, add_recipe_to_day_view, edit_user_recipe_view,
                                delete_user_recipe_view, analyze_food_view, add_recipe_to_day_llm_view,
                                handle_profile_form_view, handle_target_calories_form_view, create_recipe_llm_view
                                )
from frontend.api.views import api_homepage
from frontend.ajax_views import ajax_search_recipes, ajax_suggest_food_view
from profiles.views import login_view, register_view, logout_view
from profiles.api.views import UserRegisterApiView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", homepage, name="homepage"),
    path('recipes/', recipes_list_view, name="recipe_list"),
    path('recipe/create/', create_recipe_form_view, name="recipe_create"),
    path("today/", today_data_view, name="today_data"),
    path("history/", history_view, name="history"),
    path("account/", account_view, name="account"),
    path("stats/", statistics_view, name="stats"),


    # actions
    path("action/analyze-food/<int:pk>/", analyze_food_view, name="analyze_food"),
    path("action/add-recipe-llm/<int:pk>/<int:dk>/<int:qty>/", add_recipe_to_day_llm_view, name="add_recipe_to_day_llm"),
    path("action/create-day-category/<int:pk>/<int:dk>/", create_day_category_view, name="create_day_category"),
    path("action/add-recipe/<int:pk>/<int:dk>/", add_recipe_to_day_view, name="add_recipe_to_day"),
    path('ajax/search-recipes/<int:pk>/', ajax_search_recipes, name="ajax_search_recipes"),
    path("ajax/suggest-food/", ajax_suggest_food_view, name="ajax_suggest_food"),
    path("action/edit-user-recipe/<int:pk>/", edit_user_recipe_view, name="edit_user_recipe"),
    path("action/delete-user-recipe/<int:pk>/", delete_user_recipe_view, name="delete_user_recipe"),
    path("action/handle-profile-form/", handle_profile_form_view, name="handle_profile_form"),
    path("action/handle-target-calories-form/", handle_target_calories_form_view, name="handle_target_calories_form"),
    path("action/create-recipe-llm/<int:pk>/<int:dk>/<int:fk>/", create_recipe_llm_view, name="create_recipe_llm"),
    path("edit=day/<int:pk>/", day_calories_view, name="day_calories_detail"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),

    # api
    path("api/", api_homepage),
    path('api/recipes/', include('recipe.api.urls')),
    path('api/profile/', include('profiles.api.urls')),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # graphql
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
