from django.urls import path

from . import views

urlpatterns = [
    path('query/', views.query, name='query_results'),
    path('', views.home, name='home'),
]