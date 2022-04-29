from pickletools import read_long1
from rest_framework import serializers

from .models import Recipe,Material,Procedure


class RecipeListSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Recipe
        fields = ('id','recipeName',)


class dummyRecipeSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Recipe
        fields = '__all__'

class MaterialDetailSerializer(serializers.ModelSerializer) :
    recipe = dummyRecipeSerializer(read_only = True)
    
    class Meta : 
        model = Material
        fields = '__all__'
        read_only_fields = ('recipe',)

class ProcedureDetailSerializer(serializers.ModelSerializer) :
    recipe = dummyRecipeSerializer(read_only = True)
    
    class Meta : 
        model = Procedure
        fields = '__all__'
        read_only_fields = ('recipe',)

class MaterialSerializer(serializers.ModelSerializer) :    
    class Meta : 
        model = Material
        fields = '__all__'
        read_only_fields = ('recipe',)

class ProcedureSerializer(serializers.ModelSerializer) :
    # recipe = dummyRecipeSerializer(read_only = True)
    
    class Meta : 
        model = Procedure
        fields = '__all__'
        # read_only_fields = ('recipe',)

class RecipeSerializer(serializers.ModelSerializer) :
    procedure_set = ProcedureSerializer(many=True,read_only=True)
    material_set = MaterialSerializer(many=True,read_only=True)

    material_count = serializers.IntegerField(source='material_set.count',read_only=True)
    class Meta :
        model = Recipe
        fields = '__all__'