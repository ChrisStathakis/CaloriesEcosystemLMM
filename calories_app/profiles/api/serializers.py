from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import Sum, Avg
from rest_framework_simplejwt.tokens import RefreshToken, Token

from profiles.models import Profile, TargetCalories
from planning.models import DayCalories, DayCategory
import datetime

User = get_user_model()


class ProfileSerializer(ModelSerializer):

    class Meta:
        model = Profile
        fields = ["user", "height", "weight", "activity_lvl", "year_of_birth", "calories", "bmr", "age", "gender", "id"]


class TargetCaloriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TargetCalories
        fields = ['calories', 'profile', 'target', 'protein']

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password',]
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):

        username_exists = User.objects.filter(username=data['username']).exists()
        email_exists = User.objects.filter(email=data['email']).exists()
        if username_exists or email_exists:
            raise serializers.ValidationError("Username or Email exists.")
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        refresh = RefreshToken.for_user(user)
        profile, created = Profile.objects.get_or_create(user=user)
        data = {
            'access_token': refresh.access_token,
            'refresh_token': str(refresh),
            'username': user.username,
            'email': user.email,
            'profile_id': profile.id
        }
        return data


class HomepageSerializer(serializers.Serializer):
    last_7_days_calories = serializers.IntegerField()
    this_month_calories = serializers.IntegerField()
    today_calories = serializers.IntegerField()
    target_calories = serializers.IntegerField()
    category_data = serializers.JSONField()

    @classmethod
    def build(cls, profile):
        last_days = DayCalories.objects.filter(profile=profile)[:7]
        last_days_calories = last_days.aggregate(Sum('calories'))['calories__sum'] or 0
        this_month_qs = DayCalories.objects.filter(date__month=datetime.datetime.today().month)
        this_month_calories = this_month_qs.aggregate(Sum('calories'))['calories__sum'] or 0
        categories = DayCategory.fetch_data_per_category(profile)

        today_data, created = DayCalories.objects.get_or_create(profile=profile,
                                                                date=datetime.datetime.today())
        target_calories, created = TargetCalories.objects.get_or_create(profile=profile)
        category_data = []
        for key, value in categories.items():
            new_data = {
                "title": key,
                "calories": value['calories'],
                "carbs": value['carbs'],
                "fat": value['fat'],
                "protein": value['protein']
            }
            category_data.append(new_data)

        data = {
            'last_7_days_calories': last_days_calories,
            'this_month_calories': this_month_calories,
            'today_calories': today_data.calories,
            'target_calories': target_calories.calories,
            'category_data': category_data
        }
        return cls(data)