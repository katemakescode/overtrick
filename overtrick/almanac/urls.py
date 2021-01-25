from django.urls import path

from . import views

app_name = 'almanac'
urlpatterns = [
    path('sessions/', views.index, name='session_list'),
    path('sessions/<int:session_id>/', views.detail, name='session_detail'),
]
