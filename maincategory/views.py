from django.shortcuts import render,get_list_or_404,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Material, Procedure, Recipe,Nation,Type
from .serializer import NationSerializer, RecipeListSerializer,RecipeSerializer,ProcedureSerializer,MaterialSerializer,MaterialDetailSerializer,NationListSerializer,TypeListSerializer,TypeSerializer
from Maincategory import serializer



@api_view(['GET'])
def nation_list(request) :
    nations = get_list_or_404(Nation)
    serializer = NationListSerializer(nations,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def nation_detail(request,nation_pk) :
    nation = get_object_or_404(Nation,pk=nation_pk)

    serializer = NationSerializer(nation)
    return Response(serializer.data)

@api_view(['GET'])
def type_list(request) :
    types = get_list_or_404(Type)
    serializer = TypeListSerializer(types,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def type_detail(request,type_pk) :
    type = get_object_or_404(Type,pk=type_pk)

    serializer = TypeSerializer(type)
    return Response(serializer.data)

@api_view(['GET'])
def recipe_list(request) :
    recipes = get_list_or_404(Recipe)
    serializer = RecipeListSerializer(recipes,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def recipe_detail(request,recipe_pk) :
    recipe = get_object_or_404(Recipe,pk=recipe_pk)

    serializer = RecipeSerializer(recipe)

    return Response(serializer.data)

@api_view(['GET'])
def material_list(request) :
    recipeBasics = get_list_or_404(Material)
    serializer = MaterialSerializer(recipeBasics,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def procedure_list(request) :
    recipeBasics = get_list_or_404(Procedure)
    serializer = ProcedureSerializer(recipeBasics,many=True)
    return Response(serializer.data)