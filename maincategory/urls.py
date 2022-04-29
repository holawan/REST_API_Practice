from django.urls import path
from . import views 

urlpatterns = [
    path('recipe/',views.recipe_list),
    path('recipe/<int:recipe_pk>',views.recipe_detail),
]
