from django.urls import path
from . import views 
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
    #필수인자
      title="Snippets API Practice",
      default_version='v1',
    
    #아래부터는 선택인자 
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)


urlpatterns = [
    path('swegger/', schema_view.with_ui('swagger')),
    path('recipes/',views.recipe_list),
    path('recipes/<int:recipe_pk>/',views.recipe_detail),
    path('types/',views.type_list),
    path('types/<int:type_pk>/',views.type_detail),
    path('nations/',views.nation_list),
    path('nations/<int:nation_pk>/',views.nation_detail),
    path('materials/',views.material_list),
    path('procedures/',views.procedure_list),
    # path('recipe/<int:recipe_pk>/materials/',views.recipe_material),
]
