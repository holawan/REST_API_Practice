from rest_framework import serializers

from .models import RecipeBasic 


class RecipeBasicListSerializer(serializers.ModelSerializer) :

    class Meta :
        model = RecipeBasic 
        fields = ('recipeName','nationName','typeName',)

class RecipeBasicSerializer(serializers.ModelSerializer) :

    class Meta :
        model = RecipeBasic 
        fields = '__all__'