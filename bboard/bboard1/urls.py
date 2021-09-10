from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('<int:rubric_id>/', views.by_rubric, name='by_rubric'),
    path('add/', views.BbCreateView.as_view(), name='add')
]