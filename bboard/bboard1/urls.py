from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('<int:rubric_id>/all', views.by_rubric, name='by_rubric'),
    path('add/', views.BbCreateView.as_view(), name='add'),
    url('announcement/(?P<pk>\d+)/edit', views.BbUpdateView.as_view(), name='edit'),
    url('announcement/(?P<pk>\d+)/delete', views.BbDeleteView.as_view(), name='delete'),
    url('announcement/(?P<pk>\d+)', views.objec.as_view(), name='obj'),
]