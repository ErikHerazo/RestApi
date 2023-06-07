from rest_framework import viewsets
from .models import Category, Type, Element
from .serializers import CategorySerializer, TypeSerializer, ElementSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all().order_by('id')
    serializer_class = TypeSerializer

class ElementViewSet(viewsets.ModelViewSet):
    queryset = Element.objects.all().order_by('id')
    serializer_class = ElementSerializer