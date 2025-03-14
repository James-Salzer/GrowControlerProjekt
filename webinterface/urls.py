from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/button_click', views.button_click, name='button_click'),
]
