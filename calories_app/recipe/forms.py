from django import forms
from .models import Recipe
from django.contrib.auth import get_user_model

User = get_user_model()

class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['style'] = "background-color: #e6e6e6"


class RecipeForm(BaseForm, forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Recipe
        fields = ['title', 'calories', 'protein', 'carbs', 'fats', 'user']
        help_texts = {
            'calories': 'Per 100g',
            'protein': 'Per 100g',
            'carbs': 'Per 100g',
            'fats': 'Per 100g',
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.created_by = self.cleaned_data['user']
        if commit:
            instance.save()
        return instance

