from django.contrib import admin

# Register your models here.
from csv import list_dialects
from django.contrib import admin
from .models import RecipeBasic
# Register your models here.


class recipeBasicAdmin(admin.ModelAdmin) :
    list_display = ('recipeName','nationName','typeName')

admin.site.register(RecipeBasic,recipeBasicAdmin)