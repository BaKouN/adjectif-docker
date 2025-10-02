from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('list/', views.list_view, name='list'),
    path('create/', views.create_view, name='create'),
    path('edit/<int:pk>/', views.edit_view, name='edit'),
    path('detail/<int:pk>/', views.detail_view, name='detail'),
]