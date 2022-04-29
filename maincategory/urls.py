from django.urls import path
from . import views 

urlpatterns = [
    path('recipeBasics/',views.basic_list),
    path('recipeBasics/<int:recipe_pk>',views.basic_detail),
]
