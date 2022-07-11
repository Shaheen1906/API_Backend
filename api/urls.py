from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('',CategoryGenereics.as_view()),
    path('UD/<Category_id>',CategorGenericsUD.as_view())
]
