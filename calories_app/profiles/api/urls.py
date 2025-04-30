from django.urls import path

from .views import profile_homepage_api_view, ProfileApiView, UserRegisterApiView

app_name = "api_profile"


urlpatterns = [
    path('', profile_homepage_api_view, name="home"),
    path('detail/', ProfileApiView.as_view(), name="profile"),
    path("register/", UserRegisterApiView.as_view(), name="register")
]