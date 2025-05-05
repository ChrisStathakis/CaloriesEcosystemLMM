from rest_framework.decorators import api_view
from django_filters import rest_framework
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import DayCaloriesSerializer, DayCategorySerializer, UserRecipeSerializer
from ..models import DayCategory, DayCalories, UserRecipe
from .filters import DateRangeFilter


@api_view(['GET'])
def planning_homepage_view(request, format=None):
    return Response({
        'day_calories': reverse('api_planning:day_calories', request=request, format=format),
        'day_categories': reverse('api_planning:day_categories', request=request, format=format),
        'user_recipes': reverse('api_planning:user_recipes', request=request, format=format),
    })


class DayCaloriesListApiView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = DayCaloriesSerializer
    filterset_fields = ['date', ]
    filterset_class = DateRangeFilter

    def get_queryset(self):
        profile = self.request.user.profile
        return DayCalories.objects.filter(profile=profile)


class DayCategoryListApiView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = DayCategorySerializer
    filterset_fields = ['category', 'day']

    def get_queryset(self):
        user = self.request.user
        return DayCategory.objects.filter(day__profile=user.profile)


class UserRecipeApiView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserRecipeSerializer

    def get_queryset(self):
        return UserRecipe.objects.filter(day_calories__profile=self.request.user.profile)










