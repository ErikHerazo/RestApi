from django.urls import include, path
from rest_framework import routers
from .viewsets import CategoryViewSet, TypeViewSet, ElementViewSet

router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet)
router.register(r'type', TypeViewSet)
router.register(r'element', ElementViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = router.urls