from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('',CategoryGenereics.as_view()),
    path('update/<Category_id>',CategoryGenericsUpdateDelete.as_view()),
    path('stateg/<State_id>', StateGenereics.as_view()),
    path('stateup/<State_id>', StateGenericsUpdateDelete.as_view())
 ]
