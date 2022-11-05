from django.urls import path

from . import views

urlpatterns = [
    path('category/', views.CategoryListCreate.as_view(), name='CategoryList'),
]