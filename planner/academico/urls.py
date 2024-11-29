from django.urls import path
from .views import ProfessorView, ProfessorReadUpdateDeleteView, DisciplinaConteudoListCreateAPIView, CursoListCreateAPIView, DisciplinaListCreateAPIView, DisciplinaListView, DisciplinaRetrieveUpdateDestroyAPIView, UserRegisterAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='user-register'),
    path('auth/', obtain_auth_token, name='api_token_auth'),
    path('professor', ProfessorView.as_view()),
    path('professor/<int:id>/', ProfessorReadUpdateDeleteView.as_view(), name='professor-detail'),
    path('curso/', CursoListCreateAPIView.as_view()),
    path('disciplina/', DisciplinaListCreateAPIView.as_view()),
    path('disciplina/', DisciplinaListView.as_view(), name='disciplina-list'),
    path('disciplina/<int:id>/', DisciplinaRetrieveUpdateDestroyAPIView.as_view()),
    path('disciplina/conteudo', DisciplinaConteudoListCreateAPIView.as_view()),
]