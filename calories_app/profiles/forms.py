from django import forms

from .models import TargetCalories, Profile, User
from recipe.forms import BaseForm


class TargetCaloriesForm(BaseForm, forms.ModelForm):
    profile = forms.ModelChoiceField(queryset=Profile.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = TargetCalories
        fields = ("target", "calories", "protein", "profile")


class ProfileForm(BaseForm, forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Profile
        fields = ("height", "weight", "activity_lvl", "gender", "year_of_birth", "user")


class LoginForm(BaseForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class RegisterForm(BaseForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

