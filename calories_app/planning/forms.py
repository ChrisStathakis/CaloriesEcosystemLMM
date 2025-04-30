from django import forms

from .models import UserRecipe, DayCategory, DayCalories, Recipe


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['style'] = "background-color: #e6e6e6"


class UserRecipeForm(BaseForm, forms.ModelForm):
    recipe = forms.ModelChoiceField(queryset = Recipe.objects.all(), widget = forms.HiddenInput())
    day_calories = forms.ModelChoiceField(queryset = DayCalories.objects.all(), widget = forms.HiddenInput())

    class Meta:
        model = UserRecipe
        fields = ['qty', 'recipe', 'category', 'day_calories']


class UserRecipeLLMForm(BaseForm):
    food = forms.CharField(label = "Food", widget = forms.TextInput(attrs={'placeholder': 'Enter food name', 'name': 'food'}))
    category = forms.ModelChoiceField(queryset = DayCategory.objects.all(), widget = forms.Select(attrs={'name': 'category'}))
