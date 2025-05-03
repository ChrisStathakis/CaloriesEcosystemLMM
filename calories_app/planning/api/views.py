from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import DayCaloriesSerializer, DayCategorySerializer, UserRecipeSerializer
from ..models import DayCategory, DayCalories, UserRecipe


@api_view(['GET'])
def planning_homepage_view(request, format=None):
    ...


class DayCaloriesListApiView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = DayCaloriesSerializer


    def get_queryset(self):
        profile = self.user.profile
        return DayCalories.objects.filter(profile=profile)




