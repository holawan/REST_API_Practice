from django.contrib import admin

# Register your models here.
from csv import list_dialects
from django.contrib import admin
from .models import Recipe,Material,Procedure
# Register your models here.


class RecipeAdmin(admin.ModelAdmin) :
    list_display = ('recipeName','nationName','typeName')

admin.site.register(Recipe,RecipeAdmin)

class MaterialAdmin(admin.ModelAdmin) :
    list_display = ('recipe','irdnt_name','irdnt_cpcty','irdnt_ty_nm')

admin.site.register(Material,MaterialAdmin)

class ProcedureAdmin(admin.ModelAdmin) :
    list_display = ('recipe','order_id','cooking_dc',)

admin.site.register(Procedure,ProcedureAdmin)