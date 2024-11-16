from django.urls import path
from .views import (
    ExercicioView, ExercicioTreinoReadUpdateDelete, TreinoExercicioView, TreinoReadView
)

urlpatterns = [
    # Endpoints para treino
    path('treinos/', TreinoExercicioView.as_view(), name='treino-list-create'),
    path('treinos/<int:pk>/', TreinoReadView.as_view(), name='treino-read'),

    # Endpoints para exercicio
    path('exercicios/', ExercicioView.as_view(), name='exercicio-list-create'),
    path('exercicios/<int:pk>/', ExercicioTreinoReadUpdateDelete.as_view(), name='exercicio-read-update-delete'),
]