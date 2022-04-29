from django.urls import path
from . import views 

urlpatterns = [
    path('recipes/',views.recipe_list),
    path('recipes/<int:recipe_pk>/',views.recipe_detail),
    path('materials/',views.material_list),
    path('procedures/',views.procedure_list),
    # path('recipe/<int:recipe_pk>/materials/',views.recipe_material),
]
