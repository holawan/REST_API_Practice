from rest_framework import serializers

from .models import Recipe


class RecipeListSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Recipe
        fields = ('recipeName','nationName','typeName',)

class RecipeSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Recipe
        fields = '__all__'