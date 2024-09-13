from django.urls import path
from .views import ProfessorView, ProfessorReadUpdateDeleteView, CursoListCreateAPIView, DisciplinaListCreateAPIView, DisciplinaRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('professor', ProfessorView.as_view()),
    path('professor/<int:id>/', ProfessorReadUpdateDeleteView.as_view(), name='professor-detail'),
    path('curso/', CursoListCreateAPIView.as_view()),
    path('disciplina/', DisciplinaListCreateAPIView.as_view()),
    path('disciplina/<int:id>/', DisciplinaRetrieveUpdateDestroyAPIView.as_view()),
]