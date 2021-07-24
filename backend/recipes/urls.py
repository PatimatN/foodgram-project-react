from rest_framework import routers

from django.urls import include, path

from .views import RecipeViewSet, TagViewSet, IngredientViewSet

router = routers.DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'tags', TagViewSet)
router.register(r'ingredients', IngredientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
