import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import DayCategory, DayCalories, UserRecipe


class DayCategoryNode(relay.Node):

    class Meta:
        model = DayCategory
        filter_fields = {
            'category': ['exact'],
            'day': ['exact'],  
        }
        interfaces = (relay.Node, )

class UserRecipeNode(relay.Node):
    class Meta:
        model = UserRecipe
        filter_fields = {
            'recipe': ['exact'],
            'category': ['exact'],
            'day_calories': ['exact'],
        }
        interfaces = (relay.Node, )


class DayCaloriesType(DjangoObjectType):
    class Meta:
        model = DayCalories
        fields = ("id", "calories", "protein", "carbs", "fats", "date")


class DayCategoryType(DjangoObjectType):
    class Meta:
        model = DayCategory
        fields = ("id", "category", "calories", "protein", "carbs", "fats")


class UserRecipeType(DjangoObjectType):
    class Meta:
        model = UserRecipe
        fields = ("id", "recipe", "category", "day_calories", "qty", "calories", "protein", "carbs", "fats")



class Query(graphene.ObjectType):
    day_category = relay.Node.Field(DayCategoryNode)
    day_categories = DjangoFilterConnectionField(DayCategoryNode)
    day_calories = graphene.List(DayCaloriesType)
    user_recipe = relay.Node.Field(UserRecipeNode)
    user_recipes = DjangoFilterConnectionField(UserRecipeNode)
    

    def resolve_day_categories(self, info, **kwargs):
        return DayCategory.objects.all()

    def resolve_day_calories(self, info, **kwargs):
        return DayCalories.objects.all()

    def resolve_user_recipes(self, info, **kwargs):
        return UserRecipe.objects.all()

    
