from django.urls import path

from . import views

urlpatterns = [
    path('sessions/', views.index, name='index'),
    path('sessions/<int:session_id>/', views.detail, name='detail'),
]
