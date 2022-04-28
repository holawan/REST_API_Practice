from csv import list_dialects
from django.contrib import admin
from .models import RECIPE_BASIC
# Register your models here.


class RECIPE_BASICAdmin(admin.ModelAdmin) :
    list_display = ('recipeName','nationName','typeName')

admin.site.register(RECIPE_BASIC,RECIPE_BASICAdmin)