import datetime

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from decimal import Decimal
from .lllm_helper import mifflin_st_jeor_bmr, harris_benedict_bmr, katch_mcardle_bmr  

User = get_user_model()

activity_multipliers = {
        'sedentary': 1.2,
        'lightly_active': 1.375,
        'moderately_active': 1.55,
        'very_active': 1.725,
        'extra_active': 1.9
    }


class Profile(models.Model):
    ACTIVITY_LVL = (
        ('sedentary', 1.2),
        ('lightly_active', 1.375),
        ('moderately_active', 1.55),
        ('very_active', 1.725),
        ('extra_active', 1.9),
    )
    GENDER_OPTIONS = (
        ("M", "MALE"),
        ("F", "FEMALE")
    )

    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name="profile")
    height = models.IntegerField(max_length=3)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    activity_lvl = models.CharField(max_length=120, choices=ACTIVITY_LVL)
    year_of_birth = models.DateField()
    calories = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    bmr = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    age = models.IntegerField(max_length=3, default=1)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS)

    def save(self, *args, **kwargs):
        if self.id:
            self.age = self.calculate_age()
            if self.gender == "M":
                self.bmr = (Decimal(66.5) + (Decimal(13.75) * Decimal(self.weight)) + (Decimal(5.003) * Decimal(self.height))
                            - (Decimal(6.75) * Decimal(self.age)))

                """
                self.bmr = (Decimal(88.362) + (Decimal(13.397) * Decimal(self.weight)) +
                            (Decimal(4.799) * Decimal(self.height)) - (Decimal(5.677) * Decimal(self.age)))
                """
            else:
                self.bmr = (10 * Decimal(self.weight)) + (Decimal(6.25) * Decimal(self.height)) - (5 * self.age) - 161
            self.calories = self.bmr * Decimal(self.get_activity_lvl_display())
            # self.calories = Decimal(self.calculate_calories())
        super().save(*args, **kwargs)


    def calculate_age(self):
        """
        Calculate exact age based on current date
        """

        today = datetime.datetime.today()
        age = today.year - self.year_of_birth.year #  int(self.year_of_birth.split("-")[0])

        # Check if birthday hasn't occurred this year
        """
        if (today.month, today.day) < (datetime.datetime.strptime(self.birth, "%Y-%m-%d").date().month,
                                       datetime.datetime.strptime(self.birth, "%Y-%m-%d").date().day):
            age -= 1
        print("age", age)
        """
        return age


    def calculate_calories(self):
        mifflin = mifflin_st_jeor_bmr(Decimal(self.weight), Decimal(self.height), Decimal(self.age), self.gender)
        harris = harris_benedict_bmr(Decimal(self.weight), Decimal(self.height), Decimal(self.age), self.gender)
        return (mifflin + harris) / 2
        


class TargetCalories(models.Model):
    OPTIONS_OF_TARGET = (
        ("A", "CALORIES FOCUS"),
        ("B", "PROTEIN FOCUS"),
        ("C", "CALORIES AND PROTEIN FOCUS")
    )
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    target = models.CharField(max_length=1, choices=OPTIONS_OF_TARGET)
    calories = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    protein = models.DecimalField(max_digits=8, decimal_places=2, default=0)


    def show_target(self):
        if self.target == "A":
            return f"Calories: {self.calories} Kcal"
        elif self.target == "B":
            return f"Protein: {self.protein} gr"
        else:
            return f"Calories: {self.calories} Kcal | Protein: {self.protein} gr"




