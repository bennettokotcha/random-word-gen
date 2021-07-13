from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('random_words', views.random),
    path('reset', views.zero),
]