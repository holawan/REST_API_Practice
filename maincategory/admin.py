from django.contrib import admin

# Register your models here.
from csv import list_dialects
from django.contrib import admin
from .models import Recipe,Material,Procedure,Nation,Type
# Register your models here.


class NationAdmin(admin.ModelAdmin) :
    list_display = ('name',)

admin.site.register(Nation,NationAdmin)

class TypeeAdmin(admin.ModelAdmin) :
    list_display = ('name',)

admin.site.register(Type,TypeeAdmin)

class RecipeAdmin(admin.ModelAdmin) :
    list_display = ('recipeName','nation','type')

admin.site.register(Recipe,RecipeAdmin)

class MaterialAdmin(admin.ModelAdmin) :
    list_display = ('recipe','irdnt_name','irdnt_cpcty','irdnt_ty_nm')

admin.site.register(Material,MaterialAdmin)

class ProcedureAdmin(admin.ModelAdmin) :
    list_display = ('recipe','order_id','cooking_dc',)

admin.site.register(Procedure,ProcedureAdmin)