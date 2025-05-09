# Generated by Django 4.2 on 2025-03-31 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrecipe',
            name='day_calories',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='user_recipes', to='planning.daycalories'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userrecipe',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_category_recipes', to='planning.daycategory'),
        ),
    ]
