from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import CategorySerializer, TypeSerializer, ElementSerializer
from .models import Category, Type, Element
from django.shortcuts import get_object_or_404

class ElementViewSet(viewsets.ModelViewSet):
    queryset = Element.objects.all().order_by('id')
    serializer_class = ElementSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def elements(self, request, pk=None):
        queryset = Element.objects.filter(category_id=pk).order_by('id')
        serializer = ElementSerializer(queryset, many=True)
        return Response(serializer.data)

    """def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
"""
class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all().order_by('id')
    serializer_class = TypeSerializer

    @action(detail=True, methods=['get'])
    def elements(self, request, pk=None):
        queryset = Element.objects.filter(type_id=pk).order_by('id')
        serializer = ElementSerializer(queryset, many=True)
        return Response(serializer.data)