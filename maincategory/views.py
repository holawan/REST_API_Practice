from django.shortcuts import render,get_list_or_404,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import RecipeBasic
from .serializer import RecipeBasicListSerializer,RecipeBasicSerializer
from Maincategory import serializer


@api_view(['GET'])
def basic_list(request) :
    recipeBasics = get_list_or_404(RecipeBasic)
    serializer = RecipeBasicListSerializer(recipeBasics,many=True)
    return Response(serializer.data)

@api_view(['GET'])

def basic_detail(request,recipe_pk) :
    recipeBasic = get_object_or_404(RecipeBasic,pk=recipe_pk)

    serializer = RecipeBasicSerializer(recipeBasic)

    return Response(serializer.data)