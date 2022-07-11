import imp
from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *
# Create your views here.

class CategoryGenereics(generics.ListAPIView,generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    
class CategorGenericsUD(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    lookup_field = 'Category_id'
    