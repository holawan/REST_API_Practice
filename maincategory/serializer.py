from rest_framework import serializers
from .models import Recipe,Material,Procedure,Type,Nation


class TypeListSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Type
        fields = '__all__'

class NationListSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Nation
        fields = '__all__'


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

class TypeSerializer(serializers.ModelSerializer) :
    recipe_set = RecipeListSerializer(many=True,read_only=True)

    recipe_count = serializers.IntegerField(source='recipe_set.count',read_only=True)
    class Meta :
        model = Type
        fields = '__all__'

class NationSerializer(serializers.ModelSerializer) :
    recipe_set = RecipeListSerializer(many=True,read_only=True)

    recipe_count = serializers.IntegerField(source='recipe_set.count',read_only=True)
    class Meta :
        model = Nation
        fields = '__all__'