from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Profile
from .serializers import UserSerializer, ProfileSerializer
from .permissions import IsOwnerPermission


User = get_user_model()


@api_view(['GET', ])
def profile_homepage_api_view(request, format=None):
    return Response({
        "access_token": reverse("token_obtain_pair", request=request, format=format),
        "token_refresh": reverse("token_obtain_pair", request=request, format=format),
        "register": reverse("api_profile:register", request=request, format=format),
        "profile": reverse("api_profile:profile", request=request, format=format),
    })


class UserRegisterApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileApiView(APIView):
    # permission_classes = [permissions.IsAuthenticated, ]

    def get_object(self):
        user = self.request.user
        print("user", user)
        profile = Profile.objects.get(user=user)
        return profile

    def get(self, request, format=None):
        profile = self.get_object()
        data = ProfileSerializer(profile)
        return data
