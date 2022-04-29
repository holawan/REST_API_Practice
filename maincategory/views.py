from django.shortcuts import render,get_list_or_404,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Recipe
from .serializer import RecipeListSerializer,RecipeSerializer
from Maincategory import serializer


@api_view(['GET'])
def recipe_list(request) :
    recipeBasics = get_list_or_404(Recipe)
    serializer = RecipeListSerializer(recipeBasics,many=True)
    return Response(serializer.data)

@api_view(['GET'])

def recipe_detail(request,recipe_pk) :
    recipeBasic = get_object_or_404(Recipe,pk=recipe_pk)

    serializer = RecipeSerializer(recipeBasic)

    return Response(serializer.data)