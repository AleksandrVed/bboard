from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='main'),
    path('<int:rubric_id>/all', views.by_rubric, name='by_rubric'),
    path('add/', views.BbCreateView.as_view(), name='add'),
    url('announcement/(?P<pk>\d+)', views.objec.as_view(), name='obj'),
    #path('<int:rubric_id>/<int:pke>', views.objec.as_view(), name='obj'),
]