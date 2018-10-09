from django.urls import path

from .views import (
    UpdateModelDetailAPIView,
    UpdateModelListAPIView
)

urlpatterns = [
    path('', UpdateModelListAPIView.as_view()),
    path('(?P<id>\d+)/', UpdateModelListAPIView.as_view())
]
