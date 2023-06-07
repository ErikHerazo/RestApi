from django.contrib import admin

from .models import Category, Type, Element

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'title'

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = 'id', 'title'

@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'description', 'category', 'type'