import graphene
from graphene import relay, ObjectType, List
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Recipe, Category


class RecipeType(DjangoObjectType):

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'calories', 'protein', 'fats', 'carbs']


class Query(ObjectType):
    all_recipes = graphene.List(RecipeType)

    def resolve_all_recipes(self, info, title=None, offset=0, limit=50, **kwargs):
        qs = Recipe.objects.all()
        if title:
            qs = Recipe.objects.filter(title__icontains=title)
        return qs[offset:offset + limit]












