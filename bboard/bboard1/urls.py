from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='main'),
    path('<int:rubric_id>/all', views.by_rubric, name='by_rubric'),
    path('add/', views.BbCreateView.as_view(), name='add'),
    url('announcement/(?P<pk>\d+)/edit', views.BbUpdateView.as_view(), name='edit'),
    url('announcement/(?P<pk>\d+)/delete', views.BbDeleteView.as_view(), name='delete'),
    url('announcement/(?P<pk>\d+)', views.objec.as_view(), name='obj'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout', ),
    path('accounts/registration/', views.registre, name='register'),
]