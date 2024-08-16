from django.urls import path
from .views import ProfessorView

urlpatterns = [
    path('professor', ProfessorView.as_view()),
]