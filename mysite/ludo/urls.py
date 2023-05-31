from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:substation_id>/', views.subindex, name="station"),
]